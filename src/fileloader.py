"""Load data from a text file.

Arguments:
    text file name/directory.

Exceptions:
    IOError if file cannot be found.

Returns:
    list of all words in a text file.
"""

import sys

def load(file_name):
    """
    Arguments:
        name of the file to open.
    
    Returns:
        list of lower case strings.
    """
    try:
        with open(file_name, encoding="UTF-8") as op_file:
            loaded_text = op_file.read().strip().split('\n')
            loaded_text = [word.lower() for word in loaded_text]
            return loaded_text
    except IOError as err:
        print(f'{err}\nCannot open {file_name}.', file=sys.stderr)
        sys.exit(1)
