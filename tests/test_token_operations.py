import unittest
from unittest.mock import mock_open, patch
from app.token_operations import tokenize, detokenize, process_tokens

class TestTokenOperations(unittest.TestCase):

    def test_tokenize(self):
        text = "This is a test."
        expected_tokens = ["This", "is", "a", "test."]
        result = tokenize(text)
        self.assertEqual(result, expected_tokens)

    def test_detokenize(self):
        tokens = ["This", "is", "a", "test."]
        expected_text = "This is a test."
        result = detokenize(tokens)
        self.assertEqual(result, expected_text)

    @patch("builtins.open", new_callable=mock_open, read_data="This is a test.")
    def test_process_tokens(self, mock_open):
        fromFile = "input.txt"
        toFile = "output.txt"
        vocab_name = "default"
        
        process_tokens(fromFile, toFile, vocab_name)
        
        mock_open.assert_called_with(toFile, 'w')
        mock_open().write.assert_called_once_with("This is a test.")

if __name__ == '__main__':
    unittest.main()