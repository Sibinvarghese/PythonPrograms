f=open("random","r")
words=[]
for lines in f:
    #remove \n
    line=lines.rstrip("\n")
    #splict by space
    word=line.split(" ")

    for w in word:
        #convert to uppercase
        words.append(w.upper())
        #convert to lowercase
        #words.append(w.lower())
print(words)