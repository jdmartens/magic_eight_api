import json
import random

def lambda_handler(event, context):
    responses = [
        "It is certain", "Without a doubt", "You may rely on it",
        "Yes definitely", "It is decidedly so", "As I see it, yes",
        "Most likely", "Yes", "Outlook good", "Signs point to yes",
        "Reply hazy try again", "Better not tell you now",
        "Ask again later", "Cannot predict now",
        "Concentrate and ask again", "Don't count on it",
        "Outlook not so good", "My sources say no",
        "Very doubtful", "My reply is no"
    ]
    
    question = event.get('queryStringParameters', {}).get('question', 'No question asked')
    response = random.choice(responses)

    allowed_origins = ['http://localhost:5173', 'http://magic-eight-ball-alb-976406237.us-east-2.elb.amazonaws.com']
    origin = event.get('headers', {}).get('Origin', '')

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
        'body': json.dumps({'answer': response}), 

    }

