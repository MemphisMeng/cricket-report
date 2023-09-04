from functions import *
import boto3, sys, logging

LOGGER = logging.getLogger(__name__)
def service(event, environment):
    env = os.environ['environment']
    try:
        female_competition_matches, female_competition_innings = extract_raw_data('https://cricsheet.org/downloads/odis_female_json.zip')
        male_competition_matches, male_competition_innings = extract_raw_data('https://cricsheet.org/downloads/odis_male_json.zip')
        matches, innings = [], []
        matches.extend(female_competition_matches)
        matches.extend(male_competition_matches)
        innings.extend(female_competition_innings)
        innings.extend(male_competition_innings)
        LOGGER.info("Data was successfully downloaded!")
    except Exception as e:
        LOGGER.error(f"Encountered error when downloading online data, error detail: {e}")
        sys.exit(1)

    try:
        to_insert_player_values = build_player_universe_value_text(matches)
        LOGGER.info('Successfully extracted player info from the match dataset!')
    except Exception as e:
        LOGGER.error(f"Encountered error when extracting player info from the match dataset, error detail: {e}")
        sys.exit(1)  

    match_columns = "balls_per_over, bowl_out, city, dates, event, gender, match_type, match_type_number, missing, officials, outcome, overs, player_of_match, players, registry, season, supersubs, team_type, teams, toss, venue, game_id"
    innings_columns = "team, overs, absent_hurt, penalty_runs, declared, forfeited, powerplays, miscounted_overs, target, super_over, game_id, innings_order"
    player_universe_columns = "name, player_id, gender"
    try: 
        match_result_create_statement = build_sql_create_statement('match_results', match_columns, ['game_id'])
        innings_create_statement = build_sql_create_statement('innings', innings_columns, ['game_id', 'innings_order'])
        player_universe_create_statement = build_sql_create_statement('player_universe', player_universe_columns, ['player_id'])
        LOGGER.info("Table creation queries were successfully created!")
    except:
        LOGGER.error(f"Encountered error when building table creation queries, error detail: {e}")
        sys.exit(1)
    
    # get the ARN of the DB clsuter
    rds_client = boto3.client('rds')
    clusters = rds_client.describe_db_clusters()
    cluster_arn = [cluster['DBClusterArn'] for cluster in clusters['DBClusters'] if cluster['DBClusterIdentifier'] == f'{env}-cricket-cluster'][0]

    # get the ARN of the Secret Manager
    secrets_manager_client = boto3.client('secretsmanager')
    secrets = secrets_manager_client.list_secrets()
    secret_arn = [secret['ARN'] for secret in secrets['SecretList'] if secret['Name'] == f'rds-credentials/cricket-db-{env}'][0]

    ## create tables
    rds_data_client = boto3.client('rds-data')
    # match results
    try:
        _ = rds_data_client.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            sql=match_result_create_statement,
            database=f'{env}-cricket-cluster'
        )
        LOGGER.info("Match_results table was successfully created!")
    except Exception as e:
        LOGGER.error(f"Encountered error when creating match_results table, error detail: {e}")
        sys.exit(1)
    # innings
    try:
        _ = rds_data_client.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            sql=innings_create_statement,
            database=f'{env}-cricket-cluster'
        )
        LOGGER.info("Ball-by-balls table was successfully created!")
    except Exception as e:
        LOGGER.error(f"Encountered error when creating ball-by-ball innings table, error detail: {e}")
        sys.exit(1)
    # player universe
    try:
        _ = rds_data_client.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            sql=player_universe_create_statement,
            database=f'{env}-cricket-cluster'
        )
        LOGGER.info("Player_universe table was successfully created!")
    except Exception as e:
        LOGGER.error(f"Encountered error when creating player_universe table, error detail: {e}")
        sys.exit(1)

    try:
        match_value_text, match_columns = build_column_value_text(matches, match_columns)
        match_result_insert_statement = build_sql_insert_statement(
            'match_results', match_columns, match_value_text
            )
        LOGGER.info('Match_result table insersion queries were successfully created!')
    except Exception as e:
        LOGGER.error(f"Encountered error when building match_result table insersion queries, error detail: {e}")
        sys.exit(1)

    try:   
        innings_value_text, innings_columns = build_column_value_text(innings, innings_columns)
        innings_insert_statement = build_sql_insert_statement(
            'innings', innings_columns, innings_value_text
        )
        LOGGER.info('Innings table insersion queries were successfully created!')
    except Exception as e:
        LOGGER.error(f"Encountered error when building innings table insersion queries, error detail: {e}")
        sys.exit(1)

    try:
        player_universe_insert_statement = build_sql_insert_statement(
            'player_universe', player_universe_columns, to_insert_player_values
        )
        LOGGER.info('Player universe table insersion queries were successfully created!')
    except Exception as e:
        LOGGER.error(f"Encountered error when building player_universe table insersion queries, error detail: {e}")
        sys.exit(1)

    ## insert
    try:
        _ = rds_data_client.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            sql=match_result_insert_statement,
            database=f'{env}-cricket-cluster',
            schema='match_results'
        )
        print('Insertions into match_results table were successfully completed!')
    except Exception as e:
        print(f"Encountered error when inserting into match_results table, error detail: {e}")
        sys.exit(1)
    # ball-by-ball innings
    try:
        _ = rds_data_client.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            sql=innings_insert_statement,
            database=f'{env}-cricket-cluster',
            schema='innings'
        )
        print('Insertions into ball-by-ball innnings table were successfully completed!')
    except Exception as e:
        print(f"Encountered error when inserting into innings table, error detail: {e}")
        sys.exit(1)
    # player universe
    try:
        _ = rds_data_client.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            sql=player_universe_insert_statement,
            database=f'{env}-cricket-cluster',
            schema='player_universe'
        )
        print('Insertions into player_universe table were successfully completed!')
    except Exception as e:
        print(f"Encountered error when inserting into player_universe table, error detail: {e}")
        sys.exit(1)