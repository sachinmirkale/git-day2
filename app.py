windows
linux
import boto3

# 1. Initialize EC2 client
ec2 = boto3.client("ec2", region_name="us-east-1")

# 2. Launch the EC2 instance
response = ec2.run_instances(
    # Amazon Linux 2023 AMI (replace with an AMI ID valid for your region)
    ImageId="ami-0c101f26f147fa7fd",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="my-key-pair",  # Name of your existing key pair (without .pem)
    SecurityGroupIds=["sg-0123456789abcdef0"],  # Replace with your Security Group ID
    SubnetId="subnet-0123456789abcdef0",  # Replace with your Subnet ID
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "My-Python-EC2-Instance"}],
        }
    ],
)

instance_id = response["Instances"][0]["InstanceId"]
print(f"Created instance: {instance_id}")

# 3. Optional: Wait until the instance is in 'running' state
print("Waiting for instance to be running...")
waiter = ec2.get_waiter("instance_running")
waiter.wait(InstanceIds=[instance_id])

print(f"Instance {instance_id} is running and ready.")
