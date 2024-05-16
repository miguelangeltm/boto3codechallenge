import json


def get_credentials(file_path):
    with open(file_path) as f:
        credentials = json.load(f)

    access_key = credentials['aws_access_key_id']
    secret_key = credentials['aws_secret_access_key']
    region_name = credentials.get('aws_default_region')

    return access_key, secret_key, region_name
