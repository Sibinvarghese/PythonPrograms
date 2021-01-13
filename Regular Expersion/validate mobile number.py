import re
f=open("mobile number","r")
w=open("validate mobile number","w")
dict={}
lst=[]
for item in f:
    data=item.rstrip("\n")
    rule = "(91)?\d{10}"
    matcher = re.fullmatch(rule,data)
    if (matcher == None):
        pass
    else:
        dict[data]=data
for k,v in dict.items():
    lst.append(v)
# for i in lst:
#     print(i)
for obj in lst:
    w.write(str(obj) +"\n")