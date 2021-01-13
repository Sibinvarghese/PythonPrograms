
f=open("complete.csv","r")
w=open("new demo covid file.txt","w")
dict={}
for line in f:
    lines=line.rstrip("\n").split(",")
    state1=lines[1]
    cases1=float(lines[4])
    if state1 not in dict:
        dict[state1]=cases1
    else:
        dict[state1]=cases1

print(dict)
#{'Kerala': '29151.0', 'Delhi': '140232.0', 'Telengana': '4111.0', 'Haryana': '38548.0', 'Rajasthan': '47272.0', 'Uttar Pradesh': '104388.0', 'Tamil Nadu': '273460.0', 'Union Territory of Ladakh': '10.0', 'Karnataka': '151449.0', 'Maharashtra': '468265.0', 'Punjab': '19856.0', 'Union Territory of Jammu and Kashmir': '4.0', 'Andhra Pradesh': '186461.0', 'Uttarakhand': '8254.0', 'Odisha': '39018.0', 'Puducherry': '4433.0', 'West Bengal': '83800.0', 'Chhattisgarh': '10407.0', 'Union Territory of Chandigarh': '1.0', 'Gujarat': '66669.0', 'Chandigarh': '1270.0', 'Himachal Pradesh': '2916.0', 'Jammu and Kashmir': '22955.0', 'Ladakh': '1592.0', 'Madhya Pradesh': '35734.0', 'Bihar': '64770.0', 'Manipur': '3093.0', 'Mizoram': '537.0', 'Andaman and Nicobar Islands': '1027.0', 'Goa': '7423.0', 'Assam': '50445.0', 'Jharkhand': '14888.0', 'Arunachal Pradesh': '1855.0', 'Tripura': '5725.0', 'Meghalaya': '929.0', 'Dadra and Nagar Haveli and Daman and Diu': '1366.0', 'Sikkim': '800.0', 'Nagaland': '2498.0', 'Telangana': '73050.0', 'Telangana***': '52466.0'}

lst=[]
for k,v in dict.items():
    lst.append((v,k))
lst=sorted(lst,reverse=True)
print(lst)

for n in lst:
    print(n)
#[('West Bengal', 83800.0), ('Uttarakhand', 8254.0), ('Uttar Pradesh', 104388.0), ('Union Territory of Ladakh', 10.0), ('Union Territory of Jammu and Kashmir', 4.0), ('Union Territory of Chandigarh', 1.0), ('Tripura', 5725.0), ('Telengana', 4111.0), ('Telangana***', 52466.0), ('Telangana', 73050.0), ('Tamil Nadu', 273460.0), ('Sikkim', 800.0), ('Rajasthan', 47272.0), ('Punjab', 19856.0), ('Puducherry', 4433.0), ('Odisha', 39018.0), ('Nagaland', 2498.0), ('Mizoram', 537.0), ('Meghalaya', 929.0), ('Manipur', 3093.0), ('Maharashtra', 468265.0), ('Madhya Pradesh', 35734.0), ('Ladakh', 1592.0), ('Kerala', 29151.0), ('Karnataka', 151449.0), ('Jharkhand', 14888.0), ('Jammu and Kashmir', 22955.0), ('Himachal Pradesh', 2916.0), ('Haryana', 38548.0), ('Gujarat', 66669.0), ('Goa', 7423.0), ('Delhi', 140232.0), ('Dadra and Nagar Haveli and Daman and Diu', 1366.0), ('Chhattisgarh', 10407.0), ('Chandigarh', 1270.0), ('Bihar', 64770.0), ('Assam', 50445.0), ('Arunachal Pradesh', 1855.0), ('Andhra Pradesh', 186461.0), ('Andaman and Nicobar Islands', 1027.0)]


for val in lst:
    w.write(str(val(lst))+"\n")