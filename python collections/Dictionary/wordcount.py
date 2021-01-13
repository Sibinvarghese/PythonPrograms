text="hello hai hello hai hello how are you"
#we split this text using split()
words=text.split(" ")
print(words)
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1

print(dict)


text="100,200,300,100,300,200,120"
words=text.split(",")
print(words)
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1

print(dict)
