//class

class Person{
    setPerson(name,age){
        this.name=name
        this.age=age
    }
    printPerson(){
        console.log(this.name)
        console.log(this.age);
    }

}

//object

var obj=new Person()

//reference

obj.setPerson("sibin",25)
obj.printPerson()


//Instance Variables (this.age and this.name are the instance variables)
//setPerson perform initializing instance variable

//constructor duty? initializing instance variable




