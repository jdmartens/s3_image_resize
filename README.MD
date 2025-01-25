# AWS Lambda Image Resizer

This repository contains an AWS Lambda function that resizes images uploaded to an S3 bucket. The resized images are then stored in a designated output S3 bucket.

## Files

- `lambda_function.py`: The main Lambda function code that handles image resizing.
- `.github/workflows/deploy.yml`: GitHub Actions workflow for CI/CD.
- `README.MD`: This file.

## Lambda Function Environment Variables

The Lambda function requires the following environment variables to be set:

- `DES_BUCKET`: The name of the S3 bucket where resized images will be stored.
- `WIDTH`: The width to resize the image to.
- `HEIGHT`: The height to resize the image to.

## Lambda Layer

The Lambda function uses the Python Image Library (PIL), which is not included by default in AWS Lambda. You need to use a Lambda layer to include PIL. A pre-built layer from Klayers is used:

ARN: `arn:aws:lambda:us-east-2:770693421928:layer:Klayers-p312-Pillow:4`

For more information, visit the [Klayers GitHub repository](https://github.com/keithrozario/Klayers).

## CI/CD

The deployment is handled using GitHub Actions. The workflow is defined in `.github/workflows/deploy.yml`. It performs the following steps:

1. Checks out the code from the repository.
2. Configures AWS credentials.
3. Packages the Lambda function code into a zip file.
4. Deploys the Lambda function to AWS.

### Required IAM Policy

The AWS credentials used for deployment must have a policy that allows at a minimum the following actions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:UpdateFunctionCode",
                "lambda:GetFunctionConfiguration",
                "lambda:ListAliases",
                "lambda:UpdateAlias",
                "lambda:CreateAlias",
                "lambda:PublishVersion"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

## Usage
1. Upload an image to the source S3 bucket.
2. The Lambda function will automatically resize the image and upload it to the output S3 bucket.

## Requirements
- AWS Account: The Lambda function requires an AWS account with access to S3 and Lambda.
- GitHub Repository Secrets: The GitHub Actions workflow requires AWS credentials (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) configured in the secrets section of the GitHub repository environment.
- Environment Configuration: The environment configured in the GitHub repository must match the environment specified in the deploy section of deploy.yml.

## License
This project is licensed under the MIT License.