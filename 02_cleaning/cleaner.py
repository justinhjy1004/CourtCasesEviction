import re


"""
If there is an eviction judgement
Input: Judgement Information
Output: Is it eviction?
"""
def judgement_of_restitution(judgement_info):

    if type(judgement_info) != str:
        return False
    else:
        pattern = "Restitution of Premises"
        x = re.search(pattern, judgement_info)
        
        if x is None:
            return False
        else: 
            return True

def plaintiff_and_attorney(parties):

    if type(parties) != str:
        return None, None
    
    pattern = "Plaintiff (.*?)[\s]{3,}(.*?)[^\S\r\n]{2,}(.*?)\n"

    x = re.search(pattern, parties)

    if x is None:
        return None, None
    
    plaintiff = x.group(2).strip()
    attorney = x.group(3).strip()

    return plaintiff, attorney

def defendant_and_attorney(parties):

    if type(parties) != str:
        return None, None
    
    pattern = "Defendant (.*?)[\s]{3,}(.*?)[^\S\r\n]{2,}(.*?)\n"
    x = re.search(pattern, parties)

    if x is None:
        return None, None
    
    defendant = x.group(2).strip()
    attorney = x.group(3).strip()

    return defendant, attorney

"""
Identify correctly Defendant and Attorney
Input: Parties
Output: Defendant and Attorney
"""
def defendant_and_attorney(parties):

    if type(parties) != str:
        return None, None
    
    pattern = "Defendant (.*?)[\s]{3,}(.*?)[^\S\r\n]{2,}(.*?)\n"
    x = re.search(pattern, parties)

    if x is None:
        return None, None
    
    defendant = x.group(2).strip()
    attorney = x.group(3).strip()

    return defendant, attorney

"""
Helper function for get_address()
Input: text
Output: return the first half of the text
"""
def get_half(text):
    n = len(text)
    half = round(n/2)
    
    return text[:half]

"""
Obtain Defendant's Address
Input: Defendant, Attorney and Parties
Output: Defendant's address
"""
def get_address(defendant, defendant_attorney, parties):

    # Flag for attorney
    has_attorney = True

    # Type checking
    if type(defendant) != str:
        return None
    
    if type(defendant_attorney) != str:
        defendant_attorney = ""
        has_attorney = False

    if type(parties) != str:
        return None
    

    # Base matching format
    pattern = defendant + r"[^\S\r\n]{2,}" + defendant_attorney + r"[\S\s]* NE \d{5}"
    pattern = re.sub("\(", "\(", pattern)
    pattern = re.sub("\)", "\)", pattern)

    x = re.search(pattern, parties)

    # Match on different specifications
    if x is None:
        # Without ZIP Code
        pattern = defendant + "[^\S\r\n]{1,}" + defendant_attorney + "[\S\s]* NE"
        pattern = re.sub("\(", "\(", pattern)
        pattern = re.sub("\)", "\)", pattern)
        
        x = re.search(pattern, parties)

        if x is None:
            # One line address with ZIP
            pattern = defendant + "(.*?) NE \d{5}"
            pattern = re.sub("\(", "\(", pattern)
            pattern = re.sub("\)", "\)", pattern)

            x = re.search(pattern, parties)

            if x is None:
                # One line address withOUT ZIP
                pattern = defendant + "(.*?) NE"
                pattern = re.sub("\(", "\(", pattern)
                pattern = re.sub("\)", "\)", pattern)


                x = re.search(pattern, parties)
                if x is None:
                    return None

    # Remove defendant and attorney from address
    address = x.group(0)

    defendant = re.sub("\(", "\(", defendant)
    defendant = re.sub("\)", "\)", defendant)

    defendant_attorney = re.sub("\(", "\(", defendant_attorney)
    defendant_attorney = re.sub("\)", "\)", defendant_attorney)

    address = re.sub(defendant, "", address).strip()
    address = re.sub(defendant_attorney, "", address).strip()

    # If has attorney, roughly get half
    if has_attorney:
        address = "".join(list(map(get_half,address.split("\n"))))

    address = re.sub("[\\s]{3,}", ", ", address)
 
    address = address.split(", Defendant ACTIVE, ")[0]
    address = address.split(", Witness ACTIVE, ")[0]
    address = address.split(", owes")[0]
    address = address.split(", Limited Representation Attorney")[0]
    
    return address  
    
"""
Given a string, remove the last character if it is comma
This is necessary due to my incompetency of getting a better 
algorithm above
Input: text
Output: text making without comma at the end
"""
def comma_correction(text):
    n = len(text)

    if text[-1] == ",":
        return text[:(n-1)]
    else:
        return text

"""
Writing address for normies
Input: address
Output: still address, but for the census
"""
def splitting_field(address):

    if type(address) != str:
        return None, None, None, None

    address = address.split(", ")
    
    if len(address) < 3:
        return None, None, None, None
    
    street = address[0]
    city = address[-2]
    state_zip = address[-1]

    state_zip = state_zip.split(" ")

    if len(state_zip) == 2:
        state = state_zip[0]
        zip = state_zip[1]
    else:
        state = state_zip[0]
        zip = None

    return street, city, state, zip


"""
See if an issue of continuance is obtained
Input: actions
Output: is it continued?
"""
def continued(actions):

    if actions is None:
        return False
    
    y = re.findall("continuance", actions, flags=re.IGNORECASE)

    if len(y) > 0:
        return True
    else:
        return False
    
"""
If writ is issued
Input: actions
Output: is write issued?
"""
def writ_of_restitution(actions):
    
    if actions is None:
        return False
    
    # This is done in a general sense, since there were identified
    # spelling errors found
    x = re.findall("writ", actions, flags=re.IGNORECASE)

    if len(x) > 0:
        return True
    else:
        return False