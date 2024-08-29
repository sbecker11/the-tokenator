import argparse
from token_operations import tokenize
from token_operations import detokenize

default_vocab = "english-24000-consistent-v1"
default_filePath = "./tokens.txt"
supported_vocabs = []

def test(vocab_name=default_vocab):
    """
    Tokenizes a short plain text phrase to create tokens and outputs the number of tokens.
    Then detokenizes the tokens to recreate the original plain text.
    Visually compare the original plain text and the recreated plain text,
    and report if they are the same or different.
    """
    phrase = "This is a test phrase."
    tokens = tokenize(phrase)
    print(f"Number of tokens: {len(tokens)}")
    recreated_phrase = detokenize(tokens)
    print(f"Original phrase: {phrase}")
    print(f"Recreated phrase: {recreated_phrase}")
    if phrase == recreated_phrase:
        print("The original and recreated phrases are the same.")
    else:
        print("The original and recreated phrases are different.")
    """
    Tokenizes a short plain text phrase to create tokens and outputs the number of tokens.
    Then detokenizes the tokens to recreate the original plain text.
    Visually compare the original plain text and the recreated plain text,
    and report if they are the same or different.
    """
    phrase = "This is a test phrase."
    tokens = tokenize(phrase)
    print(f"Number of tokens: {len(tokens)}")
    recreated_phrase = detokenize(tokens)
    print(f"Original phrase: {phrase}")
    print(f"Recreated phrase: {recreated_phrase}")
    if phrase == recreated_phrase:
        print("The original and recreated phrases are the same.")
    else:
        print("The original and recreated phrases are different.")
def list_vocabularies():
    print("Supported vocabularies:")
    for vocab in supported_vocabs:
        print(f"- {vocab}")

def main():
    parser = argparse.ArgumentParser(description="Process some text.")
    parser.add_argument('--action', type=str, choices=['tokenize', 'detokenize'], help='Action to perform')
    parser.add_argument('--text', type=str, help='Text to tokenize or detokenize')
    parser.add_argument('--vocab', type=str, default=default_vocab, help='Vocabulary name')
    parser.add_argument('--file', type=str, default=default_filePath, help='File path for tokens')
    parser.add_argument('--list', action='store_true', help='List all supported vocabularies')
    parser.add_argument('--test', action='store_true', help='Test tokenization and detokenization')

    args = parser.parse_args()

    # Call the test function with the provided arguments
    if args.test:
        test(vocab_name=args.vocab)
    if args.list:
        list_vocabularies()

    # Use the provided file path or the default one
    file_path = args.file
    vocab_name = args.vocab
    text = args.text
    action = args.action

    if action == 'tokenize':
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
        elif text:
            pass
        else:
            print("Please provide text to tokenize using --text")

        if text:
            tokens = tokenize(text, vocab_name)
            print(f"Tokens: {tokens}")
        else:
            print("Please provide text to tokenize using --text")

    elif action == 'detokenize':
        if file_path:
            with open(file_path, 'r') as file:
                tokens = file.read()
        elif text:
            tokens = text
        else:
            print("Please provide tokens to detokenize using --text")

        if text:
            detokenized_text = detokenize(tokens, vocab_name)
            print(f"Detokenized text: {detokenized_text}")
        else:
            print("Please provide text to detokenize using --text")


if __name__ == "__main__":
    main()