import re


def zipvalidate(postcode):
    
    if not postcode or not re.match(r'^\d{6}$', postcode):
        return False
   
    if postcode[0] in {'0', '5', '7', '8', '9'}:
        return False

    return true
   
