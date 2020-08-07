import boto3
import json
from json import JSONEncoder
import datetime

cc_client = boto3.client('codecommit')
cb_client = boto3.client('codebuild')

def lambda_handler(event, context):
    report_response = cb_client.batch_get_reports(reportArns=event['taskresult']['Build']['ReportArns'])
    reports = report_response['reports']
    for report in reports:
        if 'codeCoverageSummary' in report:
            response = cc_client.post_comment_for_pull_request(
                pullRequestId=event['detail']['pullRequestId'],
                repositoryName=event['detail']['repositoryNames'][0],
                beforeCommitId=event['detail']['destinationCommit'],
                afterCommitId=event['detail']['sourceCommit'],
                content=json.dumps(report['codeCoverageSummary'])
            )
        if 'testSummary' in report:
            response = cc_client.post_comment_for_pull_request(
                pullRequestId=event['detail']['pullRequestId'],
                repositoryName=event['detail']['repositoryNames'][0],
                beforeCommitId=event['detail']['destinationCommit'],
                afterCommitId=event['detail']['sourceCommit'],
                content=json.dumps(report['testSummary'])
            )
    return ""