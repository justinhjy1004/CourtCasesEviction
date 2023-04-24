import pandas as pd
import cleaner
import sys

if __name__ == '__main__':
    file = sys.argv[1]

    df = pd.read_csv(file)

    df["RESTITUTION"] = df.JUDGEMENT_INFO.apply(cleaner.judgement_of_restitution)
    df["PLAINTIFF"], df["PLAINTIFF_ATTORNEY"] = zip(*df.PARTIES.apply(cleaner.plaintiff_and_attorney))
    df["DEFENDANT"], df["DEFENDANT_ATTORNEY"] = zip(*df.PARTIES.apply(cleaner.defendant_and_attorney))
    
    df["DEFENDANTS_ADDRESS"] = df.apply(lambda x: cleaner.get_address(x.DEFENDANT, x.DEFENDANT_ATTORNEY, x.PARTIES), axis=1)

    df.to_csv("clean_" + file, index=None)
