# DevOps Project

# Description

`./templates` contains the base infrastructure you need for the project

```bash
STACK_NAME=Infrastructure
aws cloudformation deploy --template-file ./templates/infrastructure.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM
ENDPOINT=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey == 'HTTPSEndpoint'].OutputValue" --output text)
cd sample-app
git init
git chekout -b main
git add .
git commit -m "initial commit"
git remote add origin $ENDPOINT
git push -u origin main
```