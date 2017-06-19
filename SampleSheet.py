import pandas as pd
import os

def line_with(text, in_file):
    """ Get the line number of the given text string in a file

    Returns the line number of the string
    """
    with open(in_file) as fh:
        for i, line in enumerate(fh, 1):
            if text in line:
                return i

def read_sample_sheet(header_line, in_file):
    """ Read a SampleSheet.csv file into a Pandas data frame

    Returns the data frame
    """
    return pd.read_csv(in_file, header=header_line)
    


