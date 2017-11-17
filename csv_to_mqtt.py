import boto3
import csv
import json


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    if 'bucket' in event:
        bucket = event['bucket']
    else:
        raise Exception('Bucket name not provided!')

    if 'key' in event:
        key = event['key']
    else:
        raise Exception('Key not provided!')

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        this_csv = response['Body'].read().decode('utf-8').split()
    except Exception as e:
        print(
            'Error getting object {} from bucket {}. Make sure ' \
            'they exist and your bucket is in the same region as this function.'.format(
                key, bucket))
        raise e
    
    csv_data = csv.reader(this_csv)
     
    header = []
    data = []
    client = boto3.client('iot-data')
     
    for row in csv_data:
        if not header:
            header = row
        else:
            new_obj = dict()
            for ndx, h in enumerate(header):
                new_obj[h] = row[ndx]
            client.publish(
                topic='com.baseball/' + str(new_obj[header[0]]),
                qos=0,
                payload=json.dumps(new_obj)
            )