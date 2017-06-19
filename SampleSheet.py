import pandas
import os

def line_with(text, in_file):
    """ Find first occurrence of a string in the given file

    Returns the line number of the string
    """
    with open(in_file) as fh:
        for i, line in enumerate(fh, 1):
            if text in line:
                return i
