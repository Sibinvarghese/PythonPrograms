//method overloading

class Mathpg{

    add(){
        console.log("no arg method")
    }
    add(num){
        console.log("one arg method")
    }
    add(num2,num3){
        console.log("two arg method")
    }

}

var obj=new Mathpg()
//obj.add(10,20)
obj.add(10)