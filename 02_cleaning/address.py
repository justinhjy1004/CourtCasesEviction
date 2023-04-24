import pandas as pd
import cleaner
import sys

if __name__ == '__main__':
    file = sys.argv[1]

    df = pd.read_csv(file)

    df["DEFENDANTS_ADDRESS"] = df.apply(lambda x: cleaner.get_address(x.DEFENDANT, x.DEFENDANT_ATTORNEY, x.PARTIES), axis=1)

    df.to_csv(file, index=None)
