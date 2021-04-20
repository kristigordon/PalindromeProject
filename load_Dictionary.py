"""
Load a text file as a list
Arguments: 
    - Text file name (and Directory path if needed)
Exceptions: 
    - IOError if file name is not found
Returns: 
    - A list of all words in a text file in lower case
Requires:
    - Import sys 
"""
import sys

def load(file):
    # Open a text file and return a list of lower case strings
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1) 
        