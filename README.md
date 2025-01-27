# magic_eight_api

A serverless Magic 8-Ball API built with Python 3.13, AWS Lambda, and API Gateway.

## Description

This project implements a serverless Magic 8-Ball API with two endpoints:
1. Classic responses
2. Sassy responses

The API is deployed on AWS using Lambda functions and API Gateway, managed with the Serverless Framework.

## Prerequisites

- Python 3.13
- Node.js and npm (for Serverless Framework)
- AWS account and configured credentials
- Serverless Framework CLI (v4.4.9 or later)

## Installation

1. Clone the repository:
  ```sh
  git clone https://github.com/yourusername/magic_eight_api.git
  cd magic_eight_api```

2. Create and activate a virtual environment:
  ```sh
  python3.13 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

3. Install Python dependencies:
  ```sh
  pip install -r requirements.txt
  ```

4. Install Serverless Framework and its plugins:
  ```sh
  npm install
  npm install -g serverless
  ```

## Configuration

1. Update `serverless.yml` with your specific configurations.
2. Ensure your AWS credentials are properly set up.

## Deployment
Deploy the API to AWS:
  ```sh
  serverless deploy --aws-profile your-serverless-profile
  ```

## Usage

After deployment, you'll receive URLs for both endpoints. You can test them using curl or a web browser:
  ```sh
  curl "https://your-api-id.execute-api.us-east-2.amazonaws.com/dev/classic?question=Will%20it%20rain%20today?"
  curl "https://your-api-id.execute-api.us-east-2.amazonaws.com/dev/sassy?question=Should%20I%20eat%20pizza%20for%20breakfast?"
  ```

## Development

To run the functions locally:
  ```sh
  serverless invoke local -f classicResponse
  serverless invoke local -f sassyResponse
  ```

## Cleanup

To remove the deployed resources:
  ```sh
  serverless remove
  ```

## License

[MIT License](LICENSE)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- Jeremy Martens

## Acknowledgments

- Serverless Framework
- AWS Lambda and API Gateway
