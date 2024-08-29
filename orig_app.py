import tokenmonster
import sys


import logging

logging.basicConfig(level=logging.INFO)

default_vocab = "english-24000-consistent-v1"
default_filePath = "./tokens.txt"

def test(vocab_name=default_vocab):
    """
    Tokenizes a short plain text phrase to create tokens and outputs the number of tokens.
    Then detokenizes the tokens to recreate the original plain text.
    Visually compare the original plain text and the recreated plain text,
    and report if they are the same or different. 

    Parameters:
    vocab_name (str): The vocabulary name to use for tokenization - defaults to "english-24000-consistent-v1".
    """
    uncodedText = "Some text to turn into token IDs."
    tokens = tokenize(uncodedText)
    print(f"#Tokens: {len(tokens)}")
    decodedText = detokenize(tokens)
    print(f"decodedText: {decodedText}")
    print(f"uncodedText: {uncodedText}")
    diff = decodedText == uncodedText
    print(f"diff: {diff}")

        

# usage:
# python app.py help -> usage
# python app.py vocab -> list of vocab names
# python app.py test [vocab_name] -> test the vocab on a default text
# python app.py tokenize [vocab_name] [fromPlainTextFile or stdin] [toTokenizedFile or stdout]
# python app.py detokenize [vocab_name] [fromTokenizedFile or stdin] [toFPlainTextFile or stdout]
def main():
    if len(sys.argv) == 1:
        print("Usage: python app.py help")
        print("Usage: python app.py vocab_names")
        sys.exit(1)

    if sys.argv[1] == "help":
        print("Usage: python app.py vocab_names to list vocab_names")
        print("Usage: python app.py test [vocab_name]")
        print("Usage: python app.py tokenize [vocab_name] [fromPlainTextFile or stdin] [toTokenizedFile or stdout]")
        print("Usage: python app.py detokenize [vocab_name] [fromTokenizedFile or stdin] [toPlainTextFile or stdout]")
        sys.exit(0)

    if sys.argv[1] == "vocab_names":
        print("Listing vocab names...")  # Placeholder for actual vocab names
        sys.exit(0)

    import tokenmonster

    if sys.argv[1] == "test":
        vocab_name = sys.argv[2] if len(sys.argv) > 2 else default_vocab
        test(vocab_name)
        sys.exit(0)
        
    if sys.argv[1] == "tokenize":
        vocab_name = sys.argv[2] if len(sys.argv) > 2 else default_vocab
        fromFile = sys.argv[3] if len(sys.argv) > 3 else None
        toFile = sys.argv[4] if len(sys.argv) > 4 else None
        process_text(fromFile, toFile, vocab_name)
        
    if sys.argv[1] == "detokenize":
        vocab_name = sys.argv[2] if len(sys.argv) > 2 else default_vocab
        fromFile = sys.argv[3] if len(sys.argv) > 3 else None
        toFile = sys.argv[4] if len(sys.argv) > 4 else None
        process_tokens(fromFile, toFile, vocab_name)

if __name__ == "__main__":
    main()