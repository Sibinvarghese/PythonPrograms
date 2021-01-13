#1st character should be an alphabets within a to k
#second character must be number it iss divisible by 3
#following by any words
import re

rule="[a-k][369][a-zA-Z0-9]*"

pattern=input("enter variable name")

match=re.fullmatch(rule,pattern)

if(match==None):
    print("invalid variable name")
else:
    print("valid variable name ")


