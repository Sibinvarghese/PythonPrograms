//create student class has roll no ,name, total ,course
class student{
    constructor(rlno,name,course,total){
    this.rollno=rlno
    this.name=name
    this.course=course
    this.total=total
    }
    printStudent(){
        console.log(this.rollno)
        console.log(this.name)
        console.log(this.course)
        console.log(this.total)
    }

}

//create more than 5 object
var obj=new student(1,"sibin","mca",120)
var obj1=new student(2,"shahabas","btech",160)
var obj2=new student(3,"fanoob","bca",170)
var obj3=new student(4,"raju","bca",145)
var obj4=new student(5,"thagu","bca",139)
var obj5=new student(6,"mandan","bca",144)
//obj.printStudent()
//obj5.printStudent()

//store these object into an array
var arr=[]
arr.push(obj)
arr.push(obj1)
arr.push(obj2)
arr.push(obj3)
arr.push(obj4)
arr.push(obj5)

//show all values of array
//for(var stud of arr){
//    console.log(stud)
//}

//q1.print student whose course==bca
var f=arr.filter(num=>num.course=="bca")
console.log(f)

//q2.print student whose total>135
var s=arr.filter(stud=>stud.total>135)
console.log(s)

//total mark
var tot=arr.map(obj=>obj.total).reduce((obj,obj2)=>obj+obj2)
console.log(tot)

//q3.find highest total
var t=arr.map(obj=>obj.total).reduce((obj,obj2)=>obj>obj2?obj:obj2)
console.log(t)

//q4.sort all student with their total
var sth=arr.sort((obj,obj2)=>obj.total>obj2.total?-1:1)
console.log(sth)


