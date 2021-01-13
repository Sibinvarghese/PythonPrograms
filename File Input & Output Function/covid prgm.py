#create referenece
f=open("complete.csv","r")
#create emmployee dict
covid={}
#2020-01-30,Kerala,10.8505,76.2711,1.0,0,0.0,0,0,0
for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    state=data[1]
    confirmed=float(data[2])
    cured=float(data[3])
    death=float(data[4])
    if state not in covid:
        covid[state]={"state":state,"confirmed":confirmed,"cured":cured,"death":death}
    else:
        #pass

        covid[state]={"state":state,"confirmed":confirmed,"cured":cured,"death":death}
        continue

# for k,v in covid.items():
#     print(k,"=>",v)


def getdetails(**args):
    sta = args["statename"]
    prope = args["prop"]
    print(covid[sta]["state"])
    print(covid[sta][prope])

getdetails(statename="kerala", prop="recoverd")

