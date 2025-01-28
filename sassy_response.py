import random
import requests
from openai import OpenAPI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def lambda_handler(event, context):
    question = event.get('queryStringParameters', {}).get('question', 'No question asked')
    
    # Placeholder for AI-generated response
    # sassy_responses = [
    #     f"Oh please, '{question}'? How about you ask something more interesting?",
    #     f"'{question}'? Really? I thought you were smarter than that.",
    #     f"Let me think about '{question}'... Nah, I'd rather not.",
    #     f"'{question}'? That's what keeps you up at night? Wow.",
    #     f"I could answer '{question}', but where's the fun in that?"
    # ]
    
    # response = random.choice(sassy_responses)
    
    # return {
    #     'statusCode': 200,
    #     'body': f'Question: {question}\nSassy Answer: {response}'
    # }

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sarcastic assistant. Provide a witty and sarcastic response to the user's question."},
            {"role": "user", "content": question}
        ]
    )
    
    sarcastic_answer = response.choices[0].message.content

    return {
        'statusCode': 200,
        'body': json.dumps({'answer': sarcastic_answer})
    }

