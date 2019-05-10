import json
#import requests
import boto3
import os
from datetime import datetime
from urllib.parse import unquote_plus

var_dynamo_table_name = 'bioarxiv-sanity-state'

def get_last_run_date(dynamo_client, category_name):
    last_run_date = datetime.strptime('1900-01-01', '%Y-%m-%d')
    # get state from Dynamo for this category
    dyn_response = dynamo_client.get_item(TableName=var_dynamo_table_name
                                         ,Key={'categorykey': {'S':category_name}})
    if dyn_response is not None:
        last_run_date = datetime.strptime(dyn_response.get('last-run-time','1900-01-01'), '%Y-%m-%d')
    return last_run_date


def lambda_handler(event, context):
    dynamo_client = boto3.client('dynamodb')
    print(f'********event={event}')
    
    try:
        if event.get('Records', None) is None:
            print("No Records in event")
            return {
                    "statusCode": 400,
                    "body": json.dumps({'IsValid': False, 'message': 'Invalid events, skipping...'})
                }
        validFiles = []
        for record in event['Records']:
            if record.get('body', None) is None:
                print('header={} message={}'.format("No body in event[Records]", str(record)))
                return {
                        "statusCode": 400,
                        "body": json.dumps({'IsValid': False, 'message': 'No events to process, skipping...'})
                }
            eventsBody = json.loads(record['body'])
            print(f'********eventbody={eventsBody}')
            # After all the error handling, get the state info
            for cat_key in eventsBody.keys():
                print('category={}'.format(cat_key))
                last_run_date = get_last_run_date(dynamo_client, cat_key)
                print('last run date={}'.format(last_run_date))
    except Exception as E:
        print("ERROR, header={}, message={}".format("lambda_handler",repr(E)))
        exit(3)
