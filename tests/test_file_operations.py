import unittest
from unittest.mock import mock_open, patch
from app.file_operations import read_tokens, write_tokens

class TestFileOperations(unittest.TestCase):

    def test_read_tokens(self):
        mock_data = "token1 token2 token3"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = read_tokens("dummy_path")
            self.assertEqual(result, mock_data)

    @patch("builtins.open", new_callable=mock_open)
    def test_write_tokens(self, mock_open):
        tokens = "token1 token2 token3"
        write_tokens("dummy_path", tokens)
        mock_open().write.assert_called_once_with(tokens)

if __name__ == '__main__':
    unittest.main()