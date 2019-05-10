import json
#import requests
import boto3
import os
import datetime
from urllib.parse import unquote_plus

var_dynamo_table_name = 'bioarxiv-sanity-state'

def get_last_run_date(dynamo_client, category_name):
    last_run_date = datetime('1900-01-01')
    # get state from Dynamo for this category
    dyn_response = dynamo_client.get_item(TableName=var_dynamo_table_name
                                         ,Key={'categorykey': category_name})
    if dyn_response is not None:
        last_run_date = datetime(dyn_response.get('last-run-time'))
    return last_run_date


def lambda_handler(event, context):
    dynamo_client = boto3.client('dynamodb')
    print(f'********event={event}')
