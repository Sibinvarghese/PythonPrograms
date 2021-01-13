f=open("employee","r")
eid=[]
ename=[]
esalary=[]
for lines in f:
    #remove \n
    line=lines.rstrip("\n")
    words=line.split(",")
    id=words[0]
    name=words[1]
    sal=words[2]
    eid.append(id)
    ename.append(name)
    esalary.append(sal)
print(eid)
print(ename)
print(esalary)