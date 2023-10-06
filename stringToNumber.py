def parse_int(num_str: str):
    num_str = num_str.replace('-', ' ').lower()
    if (num_str.isdigit()):
        new = int(num_str)
        print(new)
    else:
        print("invalid number")


parse_int('1')
parse_int('one')
