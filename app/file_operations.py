import logging

logging.basicConfig(level=logging.INFO)

def read_tokens(filePath):
    with open(filePath, "r") as file:
        tokens = file.read()
    return tokens
        
def write_tokens(tokens,filePath):
    with open(filePath, "w") as file:
        file.write(tokens)
