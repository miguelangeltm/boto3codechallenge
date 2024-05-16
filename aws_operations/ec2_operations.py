def check_ec2_public_access(ec2_client):
    instances = ec2_client.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print("Instance ID:", instance['InstanceId'])
            print("State:", instance['State']['Name'])
            if 'PublicIpAddress' in instance:
                print("public Access: Yes")
                print("Public_IP:", instance['PublicIpAddress'])
            else:
                print("public access: No")
        print()
        print("fin")
