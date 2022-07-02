import pandas as pd
import config
from os import listdir
from os.path import isfile, join

class BaseFileCreation:

    def __init__(self):
        # dir where the files sit
        self.path = config.configs['sampledir']
        self.dest = r'C:\Users\Neptune\Documents\WOVEN\NI43101'

    def create_base_df(self):
        # get a list of all the files
        files = [[f, join(self.path,f)] for f in listdir(self.path) if isfile(join(self.path,f))]

        # Create Dataframe
        self.df = pd.DataFrame(files, columns=['filename','_FilePath'])

        # parse out date and company into column
        self.df['company'] = self.df['filename'].str.extract(r'^\d+.\s(.*)\s[A-Z]{1}[a-z]{2}\s\d+\s\d{4}.txt')
        self.df['date'] = self.df['filename'].str.extract(r'^\d+.\s.*\s([A-Z]{1}[a-z]{2}\s\d+\s\d{4}).txt')

        print(self.df.head())

        def add_text_column(path):
            # Import the Text File
            with open(path, encoding="utf-8") as f:
                text = f.read()
            return text

        # create the text col with the contents of each file
        self.df['fulltext'] = self.df['_FilePath'].astype(str).apply(add_text_column)
        
        # remove the path field
        self.df = self.df[['filename','company','date','fulltext']]    
    
    def create_csv(self):
        self.df.to_csv(join(self.dest,"to_upload.csv"), index=False, encoding='utf-8')

if __name__ == '__main__':
    pg = BaseFileCreation()
    pg.create_base_df()
    print(pg.df.head())
    pg.create_csv()