import re
f=open("vehicle register number", "r")
w=open("valid Veh Numbers","w")
dict={}
lst=[]
for item in f:
    data=item.rstrip("\n")
    rule="kl\d{1,2}[a-z]{2}[0-9]{3,4}"
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
# #     print(i)
for obj in lst:
    w.write(str(obj) +"\n")