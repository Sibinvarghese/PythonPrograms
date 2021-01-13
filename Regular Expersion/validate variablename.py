import re
f=open("variables","r")
w=open("valid variablenames","w")
dict={}
lst=[]
for item in f:
    data=item.rstrip("\n")
    rule = "[a-z][369][a-zA-Z0-9]*"
    matcher = re.fullmatch(rule,data)
    if (matcher == None):
        pass
    else:
        dict[data]=data
for k,v in dict.items():
    lst.append(v)
# # for i in lst:
# #     print(i)
for obj in lst:
    w.write(str(obj) +"\n")