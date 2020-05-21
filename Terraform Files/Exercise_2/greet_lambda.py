import os

def lambda_handler(event, context):
    print("Hello Terraform")
    return "{} from Lambda!".format(os.environ['greeting'])
