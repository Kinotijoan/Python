import re


def kebabize(st):
  
    pattern = r'([a-z0-9])([A-Z])|([A-Z]+)|([A-Z])([a-z])'

    def lower_case(match):
        if match.group(1).isdigit():
            return "-" + match.group(2).lower()
        elif match.group(1) == " ":
            return "-" + match.group(2).lower()
        else:
            return match.group(1) + "-" + match.group(2).lower()

    result = re.sub(pattern, lower_case, st)
    return result    
    

bg = "SOS"
me = kebabize(bg)
print(me)




