f=open("word","r")
temp=[]

for words in f:
    #print(words)
    #remove \n
    line=words.rstrip("\n")
    #print(line)
    #word by word splicting
    word=line.split(" ")
    #print(word)
    for wordt in word:
        temp.append(wordt)
print(temp)

for k in temp:
    print(k)