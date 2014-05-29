#!/bin/env python


import boto.ec2




regions = boto.ec2.regions()


aws_access_key_id='AKIAJNWZKQSP72YV5OEA'
aws_secret_access_key='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'
region='us-west-2'


conn = boto.ec2.connect_to_region(region,aws_access_key_id,aws_secret_access_key)
print conn

instances = conn.get_all_instances()

print instances
