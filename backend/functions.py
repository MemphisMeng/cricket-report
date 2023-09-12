from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
import json, sqlite3, os, warnings, re

def extract_raw_data(hyperlink: str) -> tuple:
    """Download the data from the data source (https://cricsheet.org/) 
    and separate it into 2 sets: matches, innings. Note that both each record in
    matches and innings sets is labeled by game_id collected from the file name; 
    "innings_order" is attached as well to innings records.

    Args:
        hyperlink (str): the URL of downloadable materials found on https://cricsheet.org/downloads/

    Returns:
        tuple: 
        - matches: list, collection of match results
        - innings: list, collection of ball-by-ball innings
    """    
    with urlopen(hyperlink) as zipfile:
        female_tournament_data = ZipFile(BytesIO(zipfile.read()))
        matches, innings = [], []
        for filename in female_tournament_data.namelist():
            if filename != 'README.txt':
                data = json.load(female_tournament_data.open(filename))
                game_id = filename.split('.')[0]
                info = data.get('info')
                inning = data.get('innings')
                info['game_id'] = game_id
                for i, item in enumerate(inning):
                    item['game_id'] = game_id
                    item['innings_order'] = i + 1
                matches.append(info)
                innings.extend(inning)

        zipfile.close()
    return matches, innings
    
def build_sql_create_statement(table_name: str, columns: str, primary_key:list=None) -> str:
    """Configure a create table query in SQL, which is the format of 
    "CREATE TABLE IF NOT EXISTS {table_name} ({columns});"

    Args:
        table_name (str): the table name to be created.
        columns (str): the column names to be included in the upcoming new table. No data types are required, column names have to be seperated by ", ".
        primary_key (list, optional): column name of the primary key(s). Defaults to None.

    Returns:
        str: complete query
    """    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    sql_raw_statement = open(
        os.path.join(__location__, "./../queries/create.sql")
    ).read()
    if primary_key:
        columns += f", PRIMARY KEY ({','.join(primary_key)})"
    create_statement = sql_raw_statement.format(table_name=table_name, columns=columns)
    return create_statement

def build_sql_insert_statement(table_name: str, columns: str, values: str) -> str:
    """Configure an insert table query in SQL, which is the format of 
    "INSERT OR REPLACE INTO {table_name} ({columns}) VALUES {values};"
    Note that this query is defaulted to replace the existing rows in the table if any upcoming entries duplicate on the primary key(s)

    Args:
        table_name (str): the table name to be created.
        columns (str): the column names to be included in the upcoming new table. No data types are required, column names have to be seperated by ", ".
        values (str): list of tuples of to-insert values, in text.

    Returns:
        str: complete query
    """    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    sql_raw_statement = open(
        os.path.join(__location__, "./../queries/insert.sql")
    ).read()
    insert_statement = sql_raw_statement.format(table_name=table_name, columns=columns, values=values)
    return insert_statement

def execute(database:str, query:str):
    """Executor of SQL query on SQLite database

    Args:
        database (str): SQLite directory, i.e.: data.db
        query (str): SQL query

    Returns:
        class 'sqlite3.Cursor': the outcome of SQL query exeuction
    """    
    if re.search('.(sqlite|sqlite3|db|db3|s3db|sl3|sql)', database) is None:
        warnings.warn("Sqlite database filename is recommended to end with .sqlite, .sqlite3, .db, .db3, .s3db, .sl3, .sql")
    try:
        conn = sqlite3.connect(database)
    except sqlite3.Error as e:
        print(e)

    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()
    print("Successfully executed query!")
    return result

def build_column_value_text(values:list, cols:str) -> tuple:
    """Reconstruct the to-insert values and the columns

    Args:
        values (list): a list of key-value pair sets on behelf of to-insert data rows
        cols (str): column names in text, split by ", "

    Returns:
        tuple:
        1. to_insert_values (str): tuple-like string, each element split by ", " complies to SQlite JSON standard, sorted by each dict's key set
        2. sorted_columns (str): sorted alphabetically, in order to align with the to_insert_values
    """    
    columns = cols.split(', ')
    to_insert_values = []
    for value in values:
        for column in columns:
            # explicitly assign None to the unfound key
            if column not in value:
                value[column] = None
        # sort the dict before converting it to text
        value_ = dict(sorted(value.items()))
        to_insert_values.append(convert_to_sql_insert_values(tuple(value_.values())))

    return ", ".join(to_insert_values), ', '.join(sorted(columns)) # sort the columns alphabetically to align with values

def convert_to_sql_insert_values(data:tuple) -> str:
    """A custom method to convert tuple data to string. The final result can be used in an SQLite insert query without bringing malformed JSON errors.

    Args:
        data (tuple): an object that needs to be converted to text

    Returns:
        str: tuple-like string, can be used in an SQLite insert query without bringing malformed JSON error.
    """    
    def format_value(value:any, surrounded=True):
        """An iterative way to convert all data types of Python objects to strings for SQLite upsertion.

        Args:
            value (any): to-format data value
            surrounded (bool, optional): A flag to signal if the result should be surrounded by a pair of single quotes. Defaults to True.

        Returns:
            str: JSON-formatted string
        """        
        if value is None:
            return "NULL"
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            escaped_quotes = value.replace('"', '""').replace('\'', '\'\'')
            return f'"{escaped_quotes}"'
        elif isinstance(value, list):
            converted_list = [format_value(item, surrounded=False) for item in value]
            if not surrounded:
                return "[" + ", ".join(converted_list) + "]"
            else:
                return "\'[" + ", ".join(converted_list) + "]\'"
        elif isinstance(value, dict):
            converted_dict = {
                format_value(key, surrounded=False): format_value(val, surrounded=False) for key, val in value.items()
            }
            if surrounded:
                return "\'{" + ", ".join([f"{k}: {v}" for k, v in converted_dict.items()]) + "}\'"
            else:
                return "{" + ", ".join([f"{k}: {v}" for k, v in converted_dict.items()]) + "}"
        else:
            return str(value)

    converted_data = [format_value(item) for item in data]
    return "(" + ", ".join(converted_data) + ")"

def build_player_universe_value_text(matches:list) -> str:
    """Extract all distinct players from the match results dataset, along with their gender and identifier;
    and convert to compatible tuple-like string for SQL upsertion

    Args:
        matches (list): list of dicts that respectively stand for the facts of an ODI game, including all participating players

    Returns:
        str: to-use VALUES part in an SQL upsert command
    """    
    player_universe = set()
    for match in matches:
        for player in match['registry']['people'].items():
            tmp = (player[0], player[1], match['gender'])
            player_universe.add(tmp)

    result = []
    for player in player_universe:
        result.append(convert_to_sql_insert_values(player))

    return ', '.join(result)