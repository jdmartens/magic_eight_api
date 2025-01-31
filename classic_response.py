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
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': 'http://localhost:5173',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type,Authorization'
        },
        'body': f'Question: {question}\nAnswer: {response}'
    }

