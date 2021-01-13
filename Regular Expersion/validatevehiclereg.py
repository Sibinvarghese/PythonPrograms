
import re
vehicle=input("enter vehicle registartion")

# rule="kl\d{1,2}[a-z]{1,2}[0-9]{1,2,3,4}"

rule="kl\d{1,2}[a-z]{2}[0-9]{3,4}"
matcher=re.fullmatch(rule,vehicle)
if(matcher==None):
    print("invalid")
else:
    print("valid")

#validate all gmail id
