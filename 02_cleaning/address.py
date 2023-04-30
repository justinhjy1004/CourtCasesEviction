import pandas as pd
import cleaner
import sys
import csv

if __name__ == '__main__':
    file = sys.argv[1]

    df = pd.read_csv(file, encoding='utf-8')

    df["DEFENDANTS_ADDRESS"] = df.apply(lambda x: cleaner.get_address(x.DEFENDANT, x.DEFENDANT_ATTORNEY, x.PARTIES), axis=1)
    df["STREET"], df["CITY"], df["STATE"], df["ZIP"] = zip(*df["DEFENDANTS_ADDRESS"].apply(cleaner.splitting_field))
    
    df.to_csv(file, index=None)
