import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    current_time = datetime.now().strftime('%Y%m%d-%H')

    try:
        response = ec2.create_snapshot(
            VolumeId='vol-089975d6b7de6eb0e', #Here you must replace the VolumeID assosiate with your instance. Go to AWS Management Console/EC2/ your instance/storage
            Description='My EC2 Snapshot',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags':[
                        {
                            'Key':'Name',
                            'Value': f"My Cloud9' underlying EC2 snapshot {current_time}" #Give the f string name of your choice 
                        }
                    ]
                }
            ]
        )
        logger.info(f"Created snapshot {json.dumps(response, default=str)}")
        
    except Exception as e:
        logger.error(f"Error creating snapshot {str(e)}")