import pandas as pd
import re
import sys

def clean_plaintiff(plaintiff, plaintiff_attorney):
    
    if type(plaintiff_attorney) != str:
        return plaintiff
    
    x = re.search("(.*?) [\s]{2,} (.*?)", plaintiff_attorney)
    
    if x is None:
        return plaintiff
    else:
        return str(plaintiff) + str(x.group(1))

def clean_plaintiff_attorney(plaintiff_attorney):
    
    if type(plaintiff_attorney) != str:
        return plaintiff_attorney
    
    x = re.search("(.*?) [\s]{2,} (.*?)", plaintiff_attorney)

    if x is None:
        return plaintiff_attorney
    else:
        return re.sub(x.group(1), "", plaintiff_attorney).strip()
    
def clean_defendant_address(defendant_attorney, defendants_address):

    if (type(defendant_attorney) != str) or (type(defendants_address) != str):
        return defendants_address
    
    x = re.search(defendant_attorney + ", (.*?) [0-9]{5}", defendants_address)

    if x is None:
        return defendants_address
    else:
        return re.sub(defendant_attorney + ", ", "",x.group(0))

if __name__ == '__main__':
    file = sys.argv[1]

    df = pd.read_csv(file)

    df.PLAINTIFF = df.apply(lambda x: clean_plaintiff(x.PLAINTIFF, x.PLAINTIFF_ATTORNEY), axis=1)
    df.PLAINTIFF_ATTORNEY = df.PLAINTIFF_ATTORNEY.apply(clean_plaintiff_attorney)
    df.DEFENDANTS_ADDRESS = df.apply(lambda x: clean_defendant_address(x.DEFENDANT_ATTORNEY, x.DEFENDANTS_ADDRESS), axis=1)

    df.to_csv("clean_" + file, index=None)
