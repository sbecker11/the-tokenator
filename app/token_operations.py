
import tokenmonster
import sys
import logging

logging.basicConfig(level=logging.INFO)

def tokenize(plain_text, vocab_name=default_vocab):
    vocab = tokenmonster.load(vocab_name)
    return vocab.tokenize(plain_text)

def detokenize(tokens, vocab_name=default_vocab):
    vocab = tokenmonster.load(vocab_name)
    plain_text = vocab.detokenize(tokens)
    return plain_text

def process_tokens(fromFile, toFile, vocab_name):
    """
    Processes tokens by reading tokens from a file or standard input, detokenizing them, 
    and then writing the resulting detokenized text to a file or printing it to standard output.

    Parameters:
    fromFile (str or None): The file path to read tokens from. If None, reads from standard input.
    toFile (str or None): The file path to write the detokenized text to. If None, prints to standard output.
    vocab_name (str): The vocabulary name to use for detokenization - defaults to "english-24000-consistent-v1".

    Returns:
    None
    """
    try:
        if fromFile:
            tokens = read_tokens(fromFile)
        else:
            tokens = sys.stdin.read()
        
        text = detokenize(tokens, vocab_name)
        
        if toFile:
            write_tokens(text, toFile)
        else:
            print(text)
        
        sys.exit(0)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        sys.exit(1)
    except IOError as e:
        logging.error(f"IO error: {e}")
        sys.exit(1)
    except ValueError as e:
        logging.error(f"Value error: {e}")
        sys.exit(1)
    except KeyError as e:
        logging.error(f"Key error: {e}")
        sys.exit(1)
    except TypeError as e:
        logging.error(f"Type error: {e}")
        sys.exit(1)
    except MemoryError as e:
        logging.error(f"Memory error: {e}")
        sys.exit(1)
    except PermissionError as e:
        logging.error(f"Permission error: {e}")
        sys.exit(1)
    except EOFError as e:
        logging.error(f"EOF error: {e}")
        sys.exit(1)
    except UnicodeDecodeError as e:
        logging.error(f"Unicode decode error: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)
        