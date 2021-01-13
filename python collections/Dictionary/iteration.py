student={"Roll no":101,"Name":"Sibin","Total":98}
#only print key
for key in student:
    print(key)

#print both key and value
for key in student:
    print(key,end="")
    print(student[key])

    #or
#============================

for key in student:
    print(key,"=",student[key])