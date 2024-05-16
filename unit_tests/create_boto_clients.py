import unittest
from unittest.mock import MagicMock
from boto_clients.boto_clients import create_boto_clients


class TestCreateBotoClients(unittest.TestCase):

    def test_create_boto_clients(self):
        # Test your access keys
        access_key = "YOUR_ACCESS_KEY"
        secret_key = "YOUR_SECRET_KEY"
        region_name = "YOUR_REGION"

        # Call function
        s3_client, ec2_client, rds_client = create_boto_clients(access_key, secret_key, region_name)

        # verify clients creation
        self.assertIsInstance(s3_client, MagicMock)
        self.assertIsInstance(ec2_client, MagicMock)
        self.assertIsInstance(rds_client, MagicMock)

        # verify config. parameters
        self.assertEqual(s3_client._client_config.access_key, access_key)
        self.assertEqual(s3_client._client_config.secret_key, secret_key)
        self.assertEqual(s3_client._client_config.region_name, region_name)
        self.assertEqual(ec2_client._client_config.access_key, access_key)
        self.assertEqual(ec2_client._client_config.secret_key, secret_key)
        self.assertEqual(ec2_client._client_config.region_name, region_name)
        self.assertEqual(rds_client._client_config.access_key, access_key)
        self.assertEqual(rds_client._client_config.secret_key, secret_key)
        self.assertEqual(rds_client._client_config.region_name, region_name)


if __name__ == '__main__':
    unittest.main()
