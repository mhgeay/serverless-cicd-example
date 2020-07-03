import os
import json
import boto3

sns_client = boto3.client('sns')

def lambda_handler(event, context):

  text_message = "Congrats! You deployed this application using a CI/CD pipeline."

  phone_number = os.environ['MY_EMAIL']

  print(f"Publishing message to SNS topic. Subscriber email: {phone_number}")
  
  try:
    publish_sns_update(text_message)
    print("Message send success.")
  except Exception as error:
    print(f"Message send failed, error: {error}")

def publish_sns_update(text_message):

  response = sns_client.publish(
      TargetArn = os.environ['SNS_TOPIC_ARN'], 
      Message=json.dumps({'default': text_message}),
      MessageStructure='json'
  )

  return response