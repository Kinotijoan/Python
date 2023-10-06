import re


def count_smiley(arr):
    pattern = r'[:;][-~]?[)D]'
    x = re.findall(pattern, ''.join(arr))
    return len(x)
