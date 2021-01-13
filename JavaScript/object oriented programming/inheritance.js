//single inheritance

class Parent{
    phone(){
        console.log("I Have Nokia 1100")
    }
}

class child extends Parent{

}

var c=new child()
c.phone()