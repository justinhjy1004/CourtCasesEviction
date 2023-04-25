import re

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

"""
Identify correctly Defendant and Attorney
Input: Parties
Output: Defendant and Attorney
"""
def defendant_and_attorney(parties):

    if type(parties) != str:
        return None, None
    
    x = re.search("Defendant (.*?)[\s]{3,}(.*?)[^\S\r\n]{2,}(.*?)\n", parties)

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
    
    # Relabel parantheses
    defendant = re.sub("\(", "\(", defendant)
    defendant = re.sub("\)", "\)", defendant)

    # Base matching format
    matching_format = defendant + r"[^\S\r\n]{2,}" + defendant_attorney + r"[\S\s]* NE \d{5}"
    
    x = re.search(matching_format, parties)

    # Match on different specifications
    if x is None:
        # Without ZIP Code
        matching_format = defendant + "[^\S\r\n]{1,}" + defendant_attorney + "[\S\s]* NE"
        x = re.search(matching_format, parties)
        if x is None:
            # One line address with ZIP
            matching_format = defendant + "(.*?) NE \d{5}"
            x = re.search(matching_format, parties)
            if x is None:
                # One line address withOUT ZIP
                matching_format = defendant + "(.*?) NE"
                x = re.search(matching_format, parties)
                if x is None:
                    return None

    # Remove defendant and attorney from address
    address = x.group(0)
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