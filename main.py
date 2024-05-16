from credentials.credentials import get_credentials
from boto_clients.boto_clients import create_boto_clients
from aws_operations.s3_operations import check_s3_public_access


def print_banner():
    banner = """
╔═╗╦ ╦╔═╗            
╠═╣║║║╚═╗            
╩ ╩╚╩╝╚═╝            
┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐   
├─┤│  │  ├┤ └─┐└─┐   
┴ ┴└─┘└─┘└─┘└─┘└─┘   
┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
│  ├─┤├┤ │  ├┴┐├┤ ├┬┘
└─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─
        Author: Miguel Angel Torres (16/05/2024)
    """
    print(banner)


if __name__ == "__main__":
    print_banner()
    access_key, secret_key, region_name = get_credentials('credentials/credentials.json')
    s3_client, ec2_client, rds_client = create_boto_clients(access_key, secret_key, region_name)
    check_s3_public_access(s3_client)
