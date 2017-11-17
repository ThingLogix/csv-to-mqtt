# ThingLogix
### AWS Lambda function to send each row of CSV data as MQTT messages

## Installation guide
Clone this repository, then zip all of the contents. Upload the zip file to AWS Lambda as a Lambda function with runtime Python 3.6. The handler should be csv_to_mqtt.lambda_handler.

### Usage instructions
To use this AWS Lambda function, once it has been installed, you must provide the bucket and key where the CSV file is in AWS S3. Below is how you should pass values to the Lambda function.
```
{
  "bucket": "thinglogix-open-source-lambdas",
  "key": "Batting.csv"
}
```
