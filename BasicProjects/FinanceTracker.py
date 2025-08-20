import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_tracker.csv"
    COLUMNS = ['date','amount','category','description']
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index = False)
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry = {
            'date': date,
            'amount':amount,
            'category':category,
            'description':description
        }
        with open(cls.CSV_FILE, 'a') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print('Entry Added')
CSV.initialize_csv()
CSV.add_entry("11-08-2004","45000","Electronics","Bought a Laptop.")