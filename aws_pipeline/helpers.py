import boto3


def get_account_id():
    # Create a STS client
    sts_client = boto3.client("sts")

    # Get the caller identity from AWS STS
    response = sts_client.get_caller_identity()

    # Extract the Account ID from the response
    account_id = response["Account"]
    return account_id


def get_region():
    # Get the current region from the Boto3 session
    return boto3.session.Session().region_name
