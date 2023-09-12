import argparse, sys
from functions import *

if __name__ == '__main__':
    """The entrance of the whole ingestion process
    """    
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', '-f', type=str)
    args = parser.parse_args()

    ## download online data
    print('=' * 100)
    print("Downloading online data...")
    try:
        female_competition_matches, female_competition_innings = extract_raw_data('https://cricsheet.org/downloads/odis_female_json.zip')
        male_competition_matches, male_competition_innings = extract_raw_data('https://cricsheet.org/downloads/odis_male_json.zip')

        matches, innings = [], []
        matches.extend(female_competition_matches)
        matches.extend(male_competition_matches)
        innings.extend(female_competition_innings)
        innings.extend(male_competition_innings)
        print("Data was successfully downloaded!")
    except Exception as e:
        print(f"Encountered error when downloading online data, error detail: {e}")
        sys.exit(1)

    ## extract player info from match dataset
    print('=' * 100)
    print('Extracting player info from the match dataset...')
    try:
        to_insert_player_values = build_player_universe_value_text(matches)
        print('Successfully extracted player info from the match dataset!')
    except Exception as e:
        print(f"Encountered error when extracting player info from the match dataset, error detail: {e}")
        sys.exit(1)  


    ## create table creation queries
    print('=' * 100)
    print("Building table creation queries...")
    match_columns = "balls_per_over, bowl_out, city, dates, event, gender, match_type, match_type_number, missing, officials, outcome, overs, player_of_match, players, registry, season, supersubs, team_type, teams, toss, venue, game_id"
    innings_columns = "team, overs, absent_hurt, penalty_runs, declared, forfeited, powerplays, miscounted_overs, target, super_over, game_id, innings_order"
    player_universe_columns = "name, player_id, gender"
    try: 
        match_result_create_statement = build_sql_create_statement('match_results', match_columns, ['game_id'])
        innings_create_statement = build_sql_create_statement('innings', innings_columns, ['game_id', 'innings_order'])
        player_universe_create_statement = build_sql_create_statement('player_universe', player_universe_columns, ['player_id'])
        print("Table creation queries were successfully created!")
    except Exception as e:
        print(f"Encountered error when building table creation queries, error detail: {e}")
        sys.exit(1)

    ## create tables
    # match_results table
    print('=' * 100)
    print("Creating tables...")
    try:
        execute(args.filename, match_result_create_statement)
        print("Match_results table was successfully created!")
    except Exception as e:
        print(f"Encountered error when creating match_results table, error detail: {e}")
        sys.exit(1)
    # ball-by-ball innings table
    try:
        execute(args.filename, innings_create_statement)
        print("Ball-by-balls table was successfully created!")
    except Exception as e:
        print(f"Encountered error when creating ball-by-ball innings table, error detail: {e}")
        sys.exit(1)
    # player_universe table
    try:
        execute(args.filename, player_universe_create_statement)
        print("Player_universe table was successfully created!")
    except Exception as e:
        print(f"Encountered error when creating player_universe table, error detail: {e}")
        sys.exit(1)

    ## create table insertion queries
    print('=' * 100)
    print("Building table insersion queries...")
    try:
        match_value_text, match_columns = build_column_value_text(matches, match_columns)
        match_result_insert_statement = build_sql_insert_statement(
            'match_results', match_columns, match_value_text
            )
        print('Match_result table insersion queries were successfully created!')
    except Exception as e:
        print(f"Encountered error when building match_result table insersion queries, error detail: {e}")
        sys.exit(1)

    try:   
        innings_value_text, innings_columns = build_column_value_text(innings, innings_columns)
        innings_insert_statement = build_sql_insert_statement(
            'innings', innings_columns, innings_value_text
        )
        print('Innings table insersion queries were successfully created!')
    except Exception as e:
        print(f"Encountered error when building innings table insersion queries, error detail: {e}")
        sys.exit(1)

    try:
        player_universe_insert_statement = build_sql_insert_statement(
            'player_universe', player_universe_columns, to_insert_player_values
        )
    except Exception as e:
        print(f"Encountered error when building player_universe table insersion queries, error detail: {e}")
        sys.exit(1)

    ## insert values into tables
    # match results
    print('=' * 100)
    print('Inserting rows into tables...')
    try:
        execute(args.filename, match_result_insert_statement)
        print('Insertions into match_results table were successfully completed!')
    except Exception as e:
        print(f"Encountered error when inserting into match_results table, error detail: {e}")
        sys.exit(1)
    # ball-by-ball innings
    try:
        execute(args.filename, innings_insert_statement)
        print('Insertions into ball-by-ball innnings table were successfully completed!')
    except Exception as e:
        print(f"Encountered error when inserting into innings table, error detail: {e}")
        sys.exit(1)
    # player universe
    try:
        execute(args.filename, player_universe_insert_statement)
        print('Insertions into player_universe table were successfully completed!')
    except Exception as e:
        print(f"Encountered error when inserting into player_universe table, error detail: {e}")
        sys.exit(1)