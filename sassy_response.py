try:
  import unzip_requirements
except ImportError:
  pass

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def lambda_handler(event, context):
    question = event.get('queryStringParameters', {}).get('question', 'No question asked')

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a sarcastic assistant. Provide a witty and sarcastic response to the user's question."},
            {"role": "user", "content": question}
        ]
    )
    
    sarcastic_answer = response.choices[0].message.content

    allowed_origins = ['http://localhost:5173', 'http://magic-eight-ball-alb-976406237.us-east-2.elb.amazonaws.com']
    origin = event.get('headers', {}).get('origin', '')

    cors_headers = {
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type,Authorization'
    }

    if origin in allowed_origins:
        cors_headers['Access-Control-Allow-Origin'] = origin
    else:
        cors_headers['Access-Control-Allow-Origin'] = allowed_origins[0]  # Default origin

    return {
        'statusCode': 200,
        'headers': cors_headers,
        'body': json.dumps({'answer': sarcastic_answer})
    }

