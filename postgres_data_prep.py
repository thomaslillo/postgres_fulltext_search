from nbformat import read
import pandas as pd
import csv
import sqlalchemy
import config
from os import listdir
from os.path import isfile, join
import re

class PostgresETL:

    def init(self):
        # dir where the files sit
        self.path = config.configs['sampledir']        

    def createDF(self):
        # get a list of all the files
        files = [[f, join(self.path,f)] for f in listdir(self.path) if isfile(join(self.path,f))]

        # Create Dataframe
        self.df = pd.DataFrame(files, columns=['FileName','FilePath'])

        # parse out date and company into column
        self.dfdf['Company'] = self.dfdf['FileName'].str.extract(r'^\d+.\s(.*)\s[A-Z]{1}[a-z]{2}\s\d+\s\d{4}.txt')
        self.dfdf['Date'] = self.dfdf['FileName'].str.extract(r'^\d+.\s.*\s([A-Z]{1}[a-z]{2}\s\d+\s\d{4}).txt')

    # for all the text files in a folder
    # with open("",r)

    # Import the Text File


    # create the company name and data columns from the name

    # read all the contents of the file into the full_text column

    # append the file to a dataframe

    # write the full dataframe to a csv - to go into postgress

if __name__ == '__main__':
    pg = PostgresETL()