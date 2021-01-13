f=open("ipl.txt","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    #no,team,matches,win,loss,pts
    id=data[0]
    team=data[1]
    matches=data[2]
    win=data[3]
    loss=data[4]
    pts=data[5]
    if id not in dict:
        dict[id]={"id":id,"team":team,"matches":matches,"win":win,"loss":loss,"points":pts}
    else:
         pass
# for k,v in dict.items():
#     print(k,"=>",v)
def getTeamdetails(**args):
    id = args["id"]
    propty = args["propty"]
    if(id in dict):
        print(dict[id]["team"])
        print(dict[id][propty])
    else:
        print("no team")


getTeamdetails(id="1",propty="id")
#sajaykannan10@gmail.com
getTeamdetails(id="2", propty="loss")
getTeamdetails(id="3", propty="points")

