import unittest
from unittest.mock import patch

# Import the functions to be tested
from process_tokens import tokenize, detokenize, process_tokens

class TestTokenator(unittest.TestCase):

    def test_tokenize(self):
        text = "This is a test."
        expected_tokens = ["This", "is", "a", "test", "."]
        result = tokenize(text)
        self.assertEqual(result, expected_tokens)

    def test_detokenize(self):
        tokens = ["This", "is", "a", "test", "."]
        expected_text = "This is a test."
        result = detokenize(tokens)
        self.assertEqual(result, expected_text)

    @patch('process_tokens.tokenize')
    @patch('process_tokens.detokenize')
    def test_process_tokens(self, mock_detokenize, mock_tokenize):
        text = "This is a test."
        vocab_name = "default"
        tokens = ["This", "is", "a", "test", "."]
        processed_text = "This is a test."

        mock_tokenize.return_value = tokens
        mock_detokenize.return_value = processed_text

        result = process_tokens(text, vocab_name)
        self.assertEqual(result, processed_text)
        mock_tokenize.assert_called_once_with(text)
        mock_detokenize.assert_called_once_with(tokens)

if __name__ == '__main__':
    unittest.main()