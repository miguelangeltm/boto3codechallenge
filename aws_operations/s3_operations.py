import json
from botocore.exceptions import ClientError

modified_buckets = []


def update_bucket_policy(s3_client, bucket_name):
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }
    policy_json = json.dumps(policy)
    s3_client.put_bucket_policy(Bucket=bucket_name, Policy=policy_json)
    modified_buckets.append(bucket_name)


def check_s3_public_access(s3_client):
    bucket_count = 1
    buckets = s3_client.list_buckets()
    print("-----------------------------")
    print("*** Current bucket status ***")
    print("-----------------------------")
    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        try:
            response = s3_client.get_bucket_policy_status(Bucket=bucket_name)
            acl = response['PolicyStatus']['IsPublic']
            if acl:
                print(f"({bucket_count}) public access is allowed in bucket '{bucket_name}'.")
                update_bucket_policy(s3_client, bucket_name)
            else:
                print(f"({bucket_count}) public access is not allowed in bucket '{bucket_name}'.")
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
                print(f"({bucket_count}) the bucket '{bucket_name}' has no defined policies.")
            else:
                print(f"({bucket_count}) Error obtaining bucket '{bucket_name}' configuration: {e}")
        bucket_count += 1
    print("-----------------------------")

    if len(modified_buckets) == 0:
        print("No bucket policies have been updated")
    else:
        print("*** Modified Buckets ***")
        for bucket_name in modified_buckets:
            print(bucket_name)
