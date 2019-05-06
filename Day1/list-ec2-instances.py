#!/usr/bin/python
import boto3

def stopAllRunningEC2Instances():
    ec2 = boto3.resource ( 'ec2' )

    instances = ec2.instances.filter (
        Filters=[ { 'Name': 'instance-state-name', 'Values': ['running'] } ] 
    )

    for instance in instances:
        print ( 'Stopping EC2 instance ==>', instance.id )
        instance.stop()

def startAllStoppedEC2Instances():
    ec2 = boto3.resource ( 'ec2' )

    instances = ec2.instances.filter (
        Filters=[ { 'Name': 'instance-state-name', 'Values': ['stopped'] } ] 
    )

    for instance in instances:
        print ( 'Starting EC2 instance ==>', instance.id )
        instance.start()

def printAllRunningEC2Instances():
    ec2 = boto3.resource ( 'ec2' )
    print ( 'EC2 instances currently running ...')

    instances = ec2.instances.filter (
        Filters=[ { 'Name': 'instance-state-name', 'Values': ['running'] } ] 
    )
    for instance in instances:
        print ( instance.id )

printAllRunningEC2Instances()
startAllStoppedEC2Instances()

