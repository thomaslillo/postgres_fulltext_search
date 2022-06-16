from nbformat import read
import pandas as pd
import csv
import sqlalchemy
import config
from os import listdir
from os.path import isfile, join
import re

# dir where the files sit
path = config.configs['sampledir']

# get a list of all the files
files = [[f, join(path,f)] for f in listdir(path) if isfile(join(path,f))]

# Create Dataframe
df = pd.DataFrame(files, columns=['FileName','FilePath'])

# parse out date and company into column
df['Company'] = df['FileName'].str.extract(r'^\d+.\s(.*)\s[A-Z]{1}[a-z]{2}\s\d+\s\d{4}.txt')
df['Date'] = df['FileName'].str.extract(r'^\d+.\s.*\s([A-Z]{1}[a-z]{2}\s\d+\s\d{4}).txt')

print(df.head)

# for all the text files in a folder
# with open("",r)

# Import the Text File


# create the company name and data columns from the name

# read all the contents of the file into the full_text column

# append the file to a dataframe

# write the full dataframe to a csv - to go into postgress