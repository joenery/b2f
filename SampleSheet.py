import pandas as pd
import os

samplesheet = "SampleSheet_170612_K00161_0142.csv"

def line_with(text, in_file):
    """ Get the line number of the given text string in a file

    Returns the line number of the string
    """
    with open(in_file) as fh:
        for i, line in enumerate(fh, 1):
            if text in line:
                return i

def read_sample_sheet(in_file):
    """ Read a SampleSheet.csv file into a Pandas data frame

    Returns the data frame
    """
    return pd.read_csv(in_file, header = line_with("[Data]", in_file))
    
sheet = read_sample_sheet(os.path.abspath(samplesheet))

samples = list(sheet.Sample_ID)

for sample in samples:
    print sample
