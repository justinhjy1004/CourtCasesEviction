import pandas as pd
import cleaner
import sys
import numpy as np

classification = ["Real", "Chapter"]

if __name__ == '__main__':
    file = sys.argv[1]

    df = pd.read_csv(file, on_bad_lines='skip',encoding='utf-8')

    print("Reading " + file + "...")

    df['flagCol'] = np.where(df["CLASSIFICATION"].str.contains('|'.join(classification)),1,0)
    df = df[df["flagCol"] == 1]
    df = df.drop(['flagCol'], axis=1)

    print("Extracting relevant information...")

    df["COURT"], df["YEAR"], df["CASE_NUM"] = zip(*df.CASE_ID.apply(cleaner.case_information))
    df["RESTITUTION"] = df.JUDGEMENT_INFO.apply(cleaner.judgement_of_restitution)
    df["PLAINTIFF"], df["PLAINTIFF_ATTORNEY"] = zip(*df.PARTIES.apply(cleaner.plaintiff_and_attorney))
    df["DEFENDANT"], df["DEFENDANT_ATTORNEY"] = zip(*df.PARTIES.apply(cleaner.defendant_and_attorney))
    df["WRIT"] = df.ACTIONS.apply(cleaner.writ_of_restitution)
    df["CONTINUED"] = df.ACTIONS.apply(cleaner.continued)
    df["DEFENDANTS_ADDRESS"] = df.apply(lambda x: cleaner.get_address(x.DEFENDANT, x.DEFENDANT_ATTORNEY, x.PARTIES), axis=1)

    print("Writing to " + "clean_" + file)

    df.to_csv("clean_" + file, index=None)

    print("Done cleaning " + file)
