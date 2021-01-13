import re
f=open("gmail file", "r")
w=open("valid gmail id","w")
dict={}
lst=[]
for item in f:
    data=item.rstrip("\n")
    rule="[a-z][a-zA-z0-9]*@[a-z]*.com"
    matcher=re.fullmatch(rule,data)
    #print(matcher)
    if(matcher==None):
        pass
    else:
        dict[data]=data
for k,v in dict.items():
    #print(k,v)
    lst.append(v)
# for i in lst:
#     print(i)
for obj in lst:
    w.write(str(obj) +"\n")