import pandas as pd
import cleaner
import sys

if __name__ == '__main__':
    file = sys.argv[1]

    df = pd.read_csv(file)

    df.PLAINTIFF = df.apply(lambda x: cleaner.clean_plaintiff(x.PLAINTIFF, x.PLAINTIFF_ATTORNEY), axis=1)
    df.PLAINTIFF_ATTORNEY = df.PLAINTIFF_ATTORNEY.apply(cleaner.clean_plaintiff_attorney)
    df.DEFENDANTS_ADDRESS = df.apply(lambda x: cleaner.clean_defendant_address(x.DEFENDANT_ATTORNEY, x.DEFENDANTS_ADDRESS), axis=1)
    df.RESTITUTION = df.JUDGEMENT_INFO.apply(cleaner.judgement_of_restitution)

    df["PLAINTIFF"], df["PLAINTIFF_ATTORNEY"] = zip(*df.PARTIES.apply(cleaner.plaintiff_and_attorney))
    df["DEFENDANT"], df["DEFENDANT_ATTORNEY"] = zip(*df.PARTIES.apply(cleaner.defendant_and_attorney))

    df.to_csv("clean_" + file, index=None)
