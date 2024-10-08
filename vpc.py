import boto3
ec2 = boto3.resource('ec2') # Create an EC2 resource
vpc_name = 'vpc-ho1' # Define the VPC name

# Check if a VPC with the specified name already exists

vpcs = list(ec2.vpcs.filter(Filters=[{'Name': 'tag:Name','Values': [vpc_name]}]))  

if vpcs:
        # If VPC exists, print its ID
    print(f"VPC '{vpc_name}' already exists with id '{vpcs[0].id}'") # Print a confirmation message

else:
        # If VPC does not exist, create a new one
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16') # Create a VPC with the specified CIDR block
    vpc.create_tags(Tags=[{'Key': 'Name', 'Value': vpc_name}]) # Tag the VPC with the specified name
    print(f"VPC '{vpc_name}' with id '{vpc.id}' has been created") # Print a confirmation message



#create vpc
#ec2 = boto3.client('ec2')
# vpc_name = 'vpc-ho1'
# vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
# vpc_id = vpc_response['Vpc']['VpcId']
# ec2.create_tags(Resources=[vpc_id], Tags =[{'Key':'Name', 'Value':'vpc_name'}]) 
# print(f"VPC '{vpc_name}' with id '{vpc_id}' has been created ")




