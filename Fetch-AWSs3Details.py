import boto3
import os

# Configure your AWS credentials (use IAM role, environment variables, or ~/.aws/credentials file)
AWS_ACCESS_KEY = ""#enter your access key
AWS_SECRET_KEY = ""#enter your secret key
BUCKET_NAME = ""#enter your bucket name
REGION_NAME = ""#enter your region
FILENAME=""#enter your path

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME,
)

def list_files_in_bucket(bucket_name):
    """List files in an S3 bucket"""
    response = s3.list_objects_v2(Bucket=bucket_name)
    #print (response)
    if "Contents" in response:
        for obj1 in response["Contents"]:
            print(obj1["Key"])
    else:
        print("Bucket is empty.")

def uploadfile(bucket_name,file_name):
    """Upload fil to s3 bucket"""
    s3.upload_file(
    Filename=file_name,
    Bucket=bucket_name,
    Key="Pythonfirstupload.png"
)

if __name__ == "__main__":
    # List files in the S3 bucket
    print("Files in S3 bucket:")
    list_files_in_bucket(BUCKET_NAME)
    uploadfile(BUCKET_NAME,FILENAME)