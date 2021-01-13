text="A B C C C"
words=text.split(" ")
print(words)
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        print("The 1St Recursive Character Is",word)
        break 