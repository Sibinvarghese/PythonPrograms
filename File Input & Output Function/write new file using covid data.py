f=open("complete.csv","r")
fout=open("newcovid19wirte.txt","w")
dict={}

for line in f:
    data=line.rstrip("\n").split(",")
    #print(data)
    state=data[1]
    casese=float(data[4])
    if(state not in dict):
        dict[state]=casese
    else:
        dict[state] = casese
# for k,v in dict.items():
#     print(k,",",v)

lst=[]
for k,v in dict.items():
    lst.append((v,k))
#
# for  val in lst:
#     fout.write(str(val))
#
#line by line writee

for  val in lst:
    fout.write(str(val)+"\n")