import json
import unittest
from unittest.mock import patch
from credentials.credentials import get_credentials


class TestGetCredentials(unittest.TestCase):

    @patch('builtins.open')
    @patch('json.load')
    def test_get_credentials(self, mock_json_load, mock_open):
        # JSON credentials mock file
        json_data = {
            "aws_access_key_id": "YOUR_ACCESS_KEY",
            "aws_secret_access_key": "YOUR_SECRET_KEY",
            "aws_default_region": "YOUR_REGION"
        }
        # mocks config
        mock_json_load.return_value = json_data
        mock_open.return_value.__enter__.return_value = None

        # Llamada a la función bajo prueba
        access_key, secret_key, region_name = get_credentials("fake_file.json")

        # verify results
        self.assertEqual(access_key, "YOUR_ACCESS_KEY")
        self.assertEqual(secret_key, "YOUR_SECRET_KEY")
        self.assertEqual(region_name, "YOUR_REGION")

    @patch('builtins.open')
    @patch('json.load')
    def test_get_credentials_missing_region(self, mock_json_load, mock_open):
        # Mock for country test
        json_data = {
            "aws_access_key_id": "YOUR_ACCESS_KEY",
            "aws_secret_access_key": "YOUR_SECRET_KEY"
        }
        # mock config
        mock_json_load.return_value = json_data
        mock_open.return_value.__enter__.return_value = None

        # call function
        access_key, secret_key, region_name = get_credentials("fake_file.json")

        # Verifying the results
        self.assertEqual(access_key, "YOUR_ACCESS_KEY")
        self.assertEqual(secret_key, "YOUR_SECRET_KEY")
        self.assertIsNone(region_name)


if __name__ == '__main__':
    unittest.main()
