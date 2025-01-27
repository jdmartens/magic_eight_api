import random
import requests

def lambda_handler(event, context):
    question = event.get('queryStringParameters', {}).get('question', 'No question asked')
    
    # Placeholder for AI-generated response
    sassy_responses = [
        f"Oh please, '{question}'? How about you ask something more interesting?",
        f"'{question}'? Really? I thought you were smarter than that.",
        f"Let me think about '{question}'... Nah, I'd rather not.",
        f"'{question}'? That's what keeps you up at night? Wow.",
        f"I could answer '{question}', but where's the fun in that?"
    ]
    
    response = random.choice(sassy_responses)
    
    return {
        'statusCode': 200,
        'body': f'Question: {question}\nSassy Answer: {response}'
    }

