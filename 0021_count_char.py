#this can count characters of your string
import string
str = input('Enter string : ')
StrL = list(str)
Allch = string.printable
count = {}
for ch in Allch : 
    count[ch] = 0
for ch in StrL :
    count[ch] += 1
for ch in Allch : 
    if count[ch] != 0 :
        print('%c occures %i time'% (ch, count[ch]))