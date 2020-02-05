import re
def rev(x):
    return x[::-1]
str = input("enter any string:")
pattern = re.compile('[\W_]')
rr = pattern.sub('', str)
print(rr)
strr = rev(rr)
print(strr)