#one by one word store the list
f=open("word","r")
lst=[]
for words in f:
    spl=words.rstrip("\n")
    word=spl.split(" ")
    for wr in word:
        lst.append(wr)
#print(lst)
#we want to sperate
for w in lst:
    print(w)
