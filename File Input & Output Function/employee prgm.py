#create referenece
f=open("employee","r")
#create emmployee dict
employee={}
#1001,ajay,24000,2,developer
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    id=data[0]
    name=data[1]
    sal=data[2]
    exp=data[3]
    des=data[4]
    if id not in employee:
        employee[id]={"id":id,"name":name,"salary":sal,"exp":exp,"desig":des}
    else:
        pass
for k,v in employee.items():
    print(k,"=>",v)


def getdetails(**args):
    eid = args["id"]
    prope = args["prop"]
    print(employee[eid]["name"])
    print(employee[eid][prope])
getdetails(id="1002", prop="exp")
getdetails(id="1002", prop="salary")
