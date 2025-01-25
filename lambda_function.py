import os
import boto3
from PIL import Image
import io

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get environment variables
    output_bucket = os.environ['DES_BUCKET']
    width = int(os.environ['WIDTH'])
    height = int(os.environ['HEIGHT'])

    # Get the source bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Download the image from S3
    response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
    image_content = response['Body'].read()
    
    # Resize the image
    with Image.open(io.BytesIO(image_content)) as img:
        resized_img = img.resize((width, height))
        
        # Save the resized image to a buffer
        buffer = io.BytesIO()
        resized_img.save(buffer, format=img.format)
        buffer.seek(0)
    
    # Upload the resized image to the output bucket
    s3_client.put_object(Bucket=output_bucket, Key=f"resized_{object_key}", Body=buffer)
    
    return {
        'statusCode': 200,
        'body': 'Image resized successfully'
    }
