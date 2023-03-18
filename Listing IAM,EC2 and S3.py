import boto3
from pprint import pprint

#IAM,EC2,S3
aws_mag_con=boto3.session.Session(profile_name="root")
iam_con_cli=aws_mag_con.client(service_name="iam",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-2")
s3_con_cli=aws_mag_con.client(service_name="s3",region_name="us-east-1")
sts_cli=aws_mag_con.client(service_name='sts',region_name="us-east-1")

#Listing all the users using client object
response_for_iam=iam_con_cli.list_users()
for each_item_iam in response_for_iam["Users"]:
    print("List of all IAM users:",each_item_iam['UserName'])
print("----------------")

#Listing all EC2 instances
response_for_EC2=ec2_con_cli.describe_instances()
for each_item in response_for_EC2['Reservations']:
    for each_instance in each_item['Instances']:
        print("The instance id is:{} \nThe image Id is: {} \nThe Launch Id is: {}".format(each_instance['InstanceId'],each_instance['ImageId'],each_instance['LaunchTime']))
    print("----------------")

#Getting Volumes associated with repective instance
response_for_vol=ec2_con_cli.describe_volumes()
for each_item in response_for_vol["Volumes"]:
    for each_vol in each_item["Attachments"]:
        print("Instance ID {} corresponding to particular volumes {}".format(each_vol['InstanceId'],each_vol['VolumeId']))
    print("The availability Zone is: ",each_item['AvailabilityZone'])
    print("-----------------")
#Listing the names of S3 buckets
response_for_S3=s3_con_cli.list_buckets()
for each_item in response_for_S3["Buckets"]:
    print("List of all s3 buckets:",each_item["Name"])
print("-------------")

#Listing identities using STS
response_for_sts=sts_cli.get_caller_identity()
print("UserId of the STS client:",response_for_sts["UserId"])
