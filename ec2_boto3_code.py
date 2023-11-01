import boto3

# create an EC2 key pair
def create_key_pair(key_pair_name):
   ec2_client = boto3.client("ec2", region_name="us-east-1")
   response = ec2_client.create_key_pair(KeyName=key_pair_name)  
   print(response)

#create_key_pair("my-ec2-key-pair")
'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAmkIVqqURoGqhROxIu8keOeI7KG46cfQiqdP9UqK3U7vXAHcl\n564imGguJdW581OLp+5hSRdNVPCIWAQSbGyjI1yWd4JTjD672Y0Hqbw2A2qnabZR\n+zcNSpqSAhs4PD6KH10Nu1DhVMiI7BCDEwCDaktKm5bv49Da8+CM4YeZ93b0HMO0\ntBPyDtFmELVj1bXKYq/zo/gl0Ub0fR93HGGd7SfAgIOmTSK1LzEwC2wZDehVXY8W\nkGm5ZfAM+s3NTthLl4FCWwhWrn0EqT+9zp1x0/exIIMquN5SJYXCxmBp5dP5TzDC\nHlSx/AxyEz8z8MKf04RnLk2X/ETvU5E8ehS3uwIDAQABAoIBAA2Ux+eQRO8EtFIn\nI3g1Cs451s+GdOrXfb3KBkGiRdW/cfx+gP3W3QDiGz4FhSuhLWiJmlMfFBXoX3iw\nUxbssahJXI4FEWoFk/BhdE1DXtYKK9co0Cr3+9mXpkc9MkRLlUmRncXiJxSZ20Q9\nZ+ziXK+dFWKBdXlvR/e0y3KHx8x7rzT64OWnaG6FbYDLM6RuC6K8n8XwNYmt9HKx\n/H7XhIxmohRijyuegh3qcIsE7+UgZCbrh8v6ACOgmH7K0sdRjkCEJEd3Q3FfFbeP\nt9Sd94KLdngRknrLyV1wcvJAdEQ5z2NPefXY1k5yvFYh9UhqIHWQRgEzzdQ+0NqB\nst49EhECgYEA5/jEXINSXT3xxkuSgDtkTpnqq5KeKr4PVqDEnBibpQcbQSG5xTwo\nzDm4vRDEXrIk/zXKP81WjRUsXm/2MaPAbW6xgccMUonLWGUZN0X578DsC9SLMpUe\nHFrkwg/H8/K6NkiIhze+z6AuRPO7xqWvOSWp7g24pfl6R1qSkOTI5XcCgYEAqjyS\nvQ7vRqTHT0cZ/wnIeVqM6YpMQAbn1p9JO7LvcEAmpyrC+kJTuKsWBZfT4Jmv74UL\nFckeK8yxwH5zFy5RNaYWcEpa1VoWyEcaksOoBydpTgChhGnAM/ZiKVKeNJxQh0H7\nfubQ+YzkWlbe8D/VKMGFISAliZFcIeyi24C2YN0CgYEArDz858gmHs+AtoCkbYwr\nxWTpZq19vTTTxLmoYlKvNpCZPvogqn8pt8HgFpndhIZ3i/tPiaIYcrbW8+PkBCWX\nGmoHaNn3n01q695dI7pUgx1W5s3Q8SThb6JZmnIHQG3or6eZn/TXO+iukkn7Edsx\nyJfbncMYaDxd+58XlngZZq8CgYBpnfMcQKvLFGhjkyVZyeQLBlbufdMY1i/4RBLX\nawiKiAJzLGCTi5sNs3eSOMRHUJKK8+wQtBp36iNN3iXhd+cCdezt9fOs8pu33gVq\nkOEqrxTyRAnxcPrCQlZcdNmaonCDujgiX2m/qd3y/nqKa8//3TCPgLZJR1n14i6Y\nKJ7+MQKBgHVsM7p3YWVz9Q2grTDTS8gvm/fT9qNmE1oR9lJLKEhxSyH/sac4ervv\ni2CZvJgYwqkqNsF+0Kawu96Vqx4Teu4Wb1ykOqWxSlMvEP1VlTQ0OpvdSpGuhRLI\n5yQchqcsboAgQ7mhcAMlDCOWuOF1FURXaqqnKp4Nhkayb/LEDa2G\n-----END RSA PRIVATE KEY-----'
# create an EC2 instance
def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-090fa75af13c156b4",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="my-ec2-key-pair"
    )
    print(f'Instance id: {instances["Instances"][0]["InstanceId"]}')
#create_instance()
# get a public key of an EC2 instance
def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(f'public IP adress: {instance.get("PublicIpAddress")}')

#get_public_ip('i-03f23a5e8d01a73c4')
# list all running EC2 instances
def get_running_instances():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")
    print("instance.id\t\tinstance_type\tpublic IP address\tprivate IP address\n")
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance.get("PublicIpAddress")
            private_ip = instance.get("PrivateIpAddress")
            print(f"{instance_id}\t{instance_type}\t{public_ip}\t\t\t{private_ip}")

# stop an EC2 instance we created.
def stop_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)

#stop_instance('i-03f23a5e8d01a73c4')
# terminate an EC2 instance
def terminate_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)

terminate_instance('i-03f23a5e8d01a73c4')





