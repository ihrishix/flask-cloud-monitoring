import boto3

ecr_client = boto3.client('ecr')

repository_name = "flask-devops-app"
response = ecr_client.create_repository(repositoryName=repository_name)

repo_uri = response['repository']['repositoryUri']
print(repo_uri)