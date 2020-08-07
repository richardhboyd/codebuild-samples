import boto3
import json

cc_client = boto3.client('codecommit')

def lambda_handler(event, context):
    response = cc_client.evaluate_pull_request_approval_rules(
        pullRequestId=event['detail']['pullRequestId'],
        revisionId=event['detail']['revisionId']
    )
    if response['evaluation']['approved']==True and len(response['evaluation']['approvalRulesNotSatisfied']) <=0:
        # response = cc_client.merge_pull_request_by_three_way(
        response = cc_client.merge_pull_request_by_fast_forward(
            pullRequestId=event['detail']['pullRequestId'],
            repositoryName=event['detail']['repositoryNames'][0]
        )
    return ""
