# AWS_Automation_using_Boto3
This repository consists of code that can automate AWS services using boto3 module using python

Before using the code we need to configure the access keys and secret access key in our local system.

We do this inorder to get access to the repective IAM user or root user

The configuration can be done using the below commands:

aws configure ---> If we use this command there is a high possibility that our access keys and secret access keys can be accesssible to everyone who uses the code

So inorder to avoid that access we need to configure the users seperately this can be done using the below command.

aws configure --profile "name"    ---> Here the name is the respective IAM user name or root name
