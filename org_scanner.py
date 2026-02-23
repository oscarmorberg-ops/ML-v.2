org = boto3.client('organizations')
accounts = org.list_accounts()
