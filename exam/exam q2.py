f=open("temp","r")
fout=open("new file.txt","w")
dict={}
for line in f:
    lines=line.rstrip("\n").split(",")
    #print(lines)
    state=lines[0]
    #print(state)
    temp=lines[1]
    #print(temp)
    if state not in dict:
        dict[state]=temp
    else:
        if(dict[state]<temp):
            dict[state]=temp
# for k,v in dict.items():
#     print(k,"=",v)
lst=[]
for k,v in dict.items():
    lst.append((k,v))
print(lst)
for details in lst:
    fout.write(str(details)+"\n")