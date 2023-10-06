#!/usr/bash/python3

from selenium import webdriver
browser = webdriver.Chrome('/This PC/C_drive/chromedrivers')
browser.get('https://www.google.com')

#
# text = input("Enter the message:")
#
# print("text * 10")
# code that concatinates 2 strings
from word2number import w2n
print w2n.word_to_num("two million three thousand nine hundred and eighty four")