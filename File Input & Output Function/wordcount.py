f=open("wordcount","r")
dict={}
for line in f:
    lines=line.rstrip("\n").split(" ")
    for word in lines:
        word=word.lower()
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1

print(dict)