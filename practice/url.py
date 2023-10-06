import re


def remove_url_anchor(url):
    pattern = r'[#]'
    list = url.split(pattern, 1)
    return del list[1]

url = "www.codewars.com#about"
m = remove_url_anchor(url)
print (m)