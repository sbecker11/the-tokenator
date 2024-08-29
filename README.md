```
the-tokenator/
    ├── README.md
    ├── requirements.txt
    ├── app/
    │   ├── __init__.py
    │   ├── tokenator.py
    │   │   ├── def test(vocab_name=default_vocab):
    │   │   └── def main():
    │   ├── file_operations.py
    │   │   ├── def read_tokens(filePath):
    │   │   └── def write_tokens(tokens, filePath):
    │   ├── text_operations.py
    │   │   └── def process_text(fromFile, toFile, vocab_name):
    │   └── token_operations.py
    │       ├── def tokenize(plain_text, vocab_name=default_vocab):
    │       ├── def detokenize(tokens, vocab_name=default_vocab):
    │       └── def process_tokens(fromFile, toFile, vocab_name):
    ├── tests/
    │   ├── __init__.py
    │   ├── test_tokenator.py
    │   │   ├── def test_main(self, mock_print):
    │   ├── test_file_operations.py
    │   │   ├── def test_read_tokens(self):
    │   │   └── def test_write_tokens(self, mock_open):
    │   ├── test_text_operations.py
    │   │   ├── def test_file_not_found_error(self, mock_open):
    │   │   ├── def test_io_error(self, mock_open):
    │   │   ├── def test_value_error(self, mock_read_tokens):
    │   │   ├── def test_key_error(self, mock_detokenize):
    │   │   ├── def test_type_error(self, mock_detokenize):
    │   │   ├── def test_memory_error(self, mock_read_tokens):
    │   │   ├── def test_permission_error(self, mock_open):
    │   │   ├── def test_eof_error(self, mock_open):
    │   │   ├── def test_unicode_decode_error(self, mock_open):
    │   │   ├── def test_unexpected_error(self, mock_read_tokens):
    │   └── test_token_operations.py
    │       ├── def test_tokenize(self):
    │       ├── def test_detokenize(self):
    │       └── def test_process_tokens(self, mock_open)
    └── tokenmonster/
        └── python/
            ├── README.md
            └── tokenmaster.py
                ├── def load(vocabulary_path):
                ├── def tokenize(self, text):
                └── def decode(self, tokens):
```