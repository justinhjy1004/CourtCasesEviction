import re

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
    
def judgement_of_restitution(judgement_info):

    if type(judgement_info) != str:
        return False
    else:
        x = re.search("Restitution of Premises", judgement_info)
        
        if x is None:
            return False
        else: 
            return True

def plaintiff_and_attorney(parties):

    if type(parties) != str:
        return None, None
    
    x = re.search("Plaintiff (.*?)[\s]{3,}(.*?)[^\S\r\n]{2,}(.*?)\n", parties)

    if x is None:
        return None, None
    
    plaintiff = x.group(2).strip()
    attorney = x.group(3).strip()

    return plaintiff, attorney

def defendant_and_attorney(parties):

    if type(parties) != str:
        return None, None
    
    x = re.search("Defendant (.*?)[\s]{3,}(.*?)[^\S\r\n]{2,}(.*?)\n", parties)

    if x is None:
        return None, None
    
    defendant = x.group(2).strip()
    attorney = x.group(3).strip()

    return defendant, attorney