import math
def solution(a):
    x = math.gcd(*a)
    result = x * len(a)
    return  result