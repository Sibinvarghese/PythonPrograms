class Parent{
    m1(){
        console.log("m1")
    }
}
class Child extends Parent{
    m2(){
        console.log("m2")
    }
}
class SubChild extends Child{
    m3(){
        console.log("m3")
    }
}

let sb=new SubChild()
sb.m3()
sb.m2()
sb.m1()


//==========================================================//
//multiple inheritance is not support in javascript in python
//===========================================================//