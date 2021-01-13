


string="HHHPPSDAAA"
dict={}
for item in string:
   if item not in dict:
       dict[item]=1
   else:
       dict[item]+=1
print(dict)
str1=""
for k,v in dict.items():
    str1=str1+str(v)+k
print(str1)
