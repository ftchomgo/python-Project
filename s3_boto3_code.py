# create Amazon s3 buckets with region name
import boto3
def create_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    response=s3_client.create_bucket(Bucket=bucket_name,
                            CreateBucketConfiguration=location)
    print(response)

create_bucket("first-utrains-bucket","us-east-1")
