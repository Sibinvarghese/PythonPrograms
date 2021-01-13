import re

mobile=input("enter mobile number")
rule="(91)?\d{10}"
matcher=re.fullmatch(rule,mobile)
if(matcher==None):
    print("Invalid mobile number")
else:
    print("valid mobile number")