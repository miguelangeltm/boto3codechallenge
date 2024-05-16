import unittest
from unittest.mock import Mock, patch
from aws_operations.s3_operations import check_s3_public_access


class TestS3Access(unittest.TestCase):

    @patch('builtins.print')
    def test_check_s3_public_access(self, mock_print):
        s3_client = Mock()
        s3_client.list_buckets.return_value = {'Buckets': [{'Name': 'test_bucket'}]}
        s3_client.get_bucket_policy_status.return_value = {'PolicyStatus': {'IsPublic': True}}
        check_s3_public_access(s3_client)
        self.assertEqual(mock_print.call_count, 3)

    @patch('builtins.print')
    @patch('builtins.len')
    def test_check_s3_public_access_no_modification(self, mock_len, mock_print):
        s3_client = Mock()
        s3_client.list_buckets.return_value = {'Buckets': [{'Name': 'test_bucket'}]}
        s3_client.get_bucket_policy_status.return_value = {'PolicyStatus': {'IsPublic': False}}
        mock_len.return_value = 0
        check_s3_public_access(s3_client)
        mock_print.assert_called_with("No bucket policies have been updated")


if __name__ == '__main__':
    unittest.main()
