from functions import *
import boto3

def service(event, environment):
    female_competition_matches, female_competition_innings = extract_raw_data('https://cricsheet.org/downloads/odis_female_json.zip')
    male_competition_matches, male_competition_innings = extract_raw_data('https://cricsheet.org/downloads/odis_male_json.zip')
    rds_client = boto3.client('rds-data')

