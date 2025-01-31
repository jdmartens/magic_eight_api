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

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': 'http://localhost:5173',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type,Authorization'
        },
        'body': json.dumps({'answer': sarcastic_answer})
    }

