import tokenmonster
import sys
import logging

logging.basicConfig(level=logging.INFO)

def process_text(fromFile, toFile, vocab_name):
    """
    Processes plain text by reading text from a file or standard input, tokenizing them, 
    and then writing the resulting tokes to a file or printing it to standard output.

    Parameters:
    fromFile (str or None): The file path to read plain text from. If None, reads from standard input.
    toFile (str or None): The file path to write the tokens to. If None, prints to standard output.
    vocab_name (str): The vocabulary name to use for tokenization - defaults to "english-24000-consistent-v1".

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
