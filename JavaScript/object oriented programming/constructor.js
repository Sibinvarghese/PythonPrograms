//constructor duty? initializing instance variable


class Person{
    constructor(name,age){
        this.name=name
        this.age=age
    }
    printPerson(){
        console.log(this.name)
        console.log(this.age);
    }

}

var obj=new Person("sibin",25)

obj.printPerson()
