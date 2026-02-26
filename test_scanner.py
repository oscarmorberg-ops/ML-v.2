import unittest
from unittest.mock import patch, MagicMock
from scanner import check_encryption

class TestA02(unittest.TestCase):
    @patch('boto3.client')
    def test_no_encryption(self, mock_s3):
        mock_s3.return_value.get_bucket_encryption.side_effect = Exception
        result = check_encryption('test-bucket')
        self.assertTrue(result['a02'])
        self.assertEqual(result['level'], 'HIGH')
        print("✅ A02 HIGH risk detekterad!")

if __name__ == '__main__':
    unittest.main()
