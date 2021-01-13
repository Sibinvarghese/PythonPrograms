//word count program

var text="hi hello hai hi hello hai hi hi hai hello"

var words=text.split(" ")
var dict={}
for(var word of words){
    if(word in dict){
        dict[word]+=1
    }
    else{
    dict[word]=1
    }
}
console.log(dict)

