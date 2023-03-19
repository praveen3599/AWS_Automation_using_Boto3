#Performing actions by selecting the given input parameters

##Modifications that needs to done to this code:
#   1.Status is not displaying before performingthe activity
#   2.After performing the activity status is not displaying correctly
#   3.What needs to be done when multiple instances are present
#   4.Handle the exception

import boto3
import botocore
import time
import sys

aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-2")

while True:
    print("\nSelect the mentioned activity \n1.start \n2.Stop \n3.Terminate \n4.Exit")
    activity=int(input("Enter the activity to be performed:"))
    
    if activity==1:
        instanceid=input("Enter instanceid inorder to perform the {} activity:".format(activity))
        #Checking the status of the instance given before performing the activity
        check=ec2_con_cli.describe_instance_status()
        for instance_state in check['InstanceStatuses']:
            for code,value in instance_state["InstanceState"].items():
                if value==0:
                    print("\nInstance is in Pending state")
                    break
                elif value==16:
                    print("\nInstance is Running")
                    break
                elif value==32:
                    print("\nInstance is Shutting-Down")
                    break
                elif value==48:
                    print("\nInstance is Terminated")
                    break
                elif value==64:
                    print("\nInstance is Stopping")
                    break
                else:
                    print("\nInstance is Stopped")
                    break
        print("\nStarting the {} instance".format(instanceid))
        try:
            instance_to_start=ec2_con_cli.start_instances(InstanceIds=[instanceid])
            time.sleep(60)
            for each_item in instance_to_start["StartingInstances"]:
                for each_instance,code in each_item["CurrentState"].items():
                    if code==16:
                        print("\nInstance Started successfully")
                    elif code==0:
                        print("\nInstance is still starting wait for few minutes")
                    else:
                        print("\nThere is a problem while starting the instance")
    
        #Need to handle this exception in deapth --> while stopping 
        except botocore.exceptions.ClientError as error:
            print("\nInstance may be in stopping state please check and try again")
            
    if activity==2:
        instanceid=input("Enter instanceid inorder to perform the {} activity:".format(activity))
        check=ec2_con_cli.describe_instance_status()
        for instance_state in check['InstanceStatuses']:
            for code,value in instance_state["InstanceState"].items():
                if value==0:
                    print("\nInstance is in Pending state")
                    break
                elif value==16:
                    print("\nInstance is Running")
                    break
                elif value==32:
                    print("\nInstance is Shutting-Down")
                    break
                elif value==48:
                    print("\nInstance is Terminated")
                    break
                elif value==64:
                    print("\nInstance is Stopping")
                    break
                else:
                    print("\nInstance is Stopped")
                    break
        print("\nStopping the {} instance".format(instanceid))
        try:
            instance_to_stop=ec2_con_cli.stop_instances(InstanceIds=[instanceid])
            time.sleep(60)
            for each_item in instance_to_stop["StoppingInstances"]:
                for each_instance,code in each_item["CurrentState"].items():
                    if code==80:
                        print("\nInstance Stopped successfully")
                    elif code==64:
                        print("\nInstance is still stopping wait for few minutes")
                    else:
                        print("\nThere is a problem while stopping the instance")

        #Need to handle this exception in deapth --> while stopping 
        except botocore.exceptions.ClientError as error:
            print("\nInstance may be in starting state please check and try again")

    if activity==3:
        instanceid=input("Enter instanceid inorder to perform the {} activity:".format(activity))
        check=ec2_con_cli.describe_instance_status()
        for instance_state in check['InstanceStatuses']:
            for code,value in instance_state["InstanceState"].items():
                if value==0:
                    print("\nInstance is in Pending state")
                    break
                elif value==16:
                    print("\nInstance is Running")
                    break
                elif value==32:
                    print("\nInstance is Shutting-Down")
                    break
                elif value==48:
                    print("\nInstance is Terminated")
                    break
                elif value==64:
                    print("\nInstance is Stopping")
                    break
                else:
                    print("\nInstance is Stopped")
                    break
        print("\nTerminating the {} instance".format(instanceid))
        try:
            instance_to_terminate=ec2_con_cli.terminate_instances(InstanceIds=[instanceid])
            time.sleep(60)
            for each_item in instance_to_terminate["TerminatingInstances"]:
                for each_instance,code in each_item["CurrentState"].items():
                    if code==48:
                        print("\nInstance Terminated successfully")
                    elif code==32:
                        print("\nInstance is still shutting-down wait for few minutes")
                    else:
                        print("\nThere is a problem while terminating the instance")

        #Need to handle this exception in deapth --> while stopping 
        except botocore.exceptions.ClientError as error:
            print("\nInstance may be in starting state please check and try again")
    
    if activity==4:
        print("\nAs there is no need to do any activity exiting")
        sys.exit()