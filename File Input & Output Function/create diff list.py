f=open("employee demo ","r" )
id=[]
name=[]
sal=[]
for line in f:
    lines=line.rstrip("\n").split(",")
    id1=lines[0]
    name1=lines[1]
    sal1=lines[2]
    id.append(id1)
    name.append(name1)
    sal.append(sal1)
print(id,name,sal)