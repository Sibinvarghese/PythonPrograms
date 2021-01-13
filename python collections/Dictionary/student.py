from builtins import print

student={"Roll no":101,"Name":"Sibin","Total":98}
print(student)
#print name only
print(student["Name"])
#check college key in the dictionary
print("College" in student)
#insert a values
student["College"]="Codexw tech"
print(student)
#update the total in 100
student["Total"]+=2
print(student)

