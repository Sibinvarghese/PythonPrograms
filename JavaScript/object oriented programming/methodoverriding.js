class Parent{
    phone(){
        console.log("I Have Nokia 1100")
    }
}

class child extends Parent{
    phone(){
        console.log("I Have Iphone")
    }

}

var c=new child()
c.phone()