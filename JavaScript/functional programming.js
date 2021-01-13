
//adding two numbers
//in use python (LAMBDA)
//f=lambda num1,num2:num1+num2

//adding two numbers
//In JavaScript use this symbols( "=>" )
var f=(num1,num2)=>num1+num2
console.log(f(100,20))

//sub two numbers
var f=(num1,num2)=>num2-num1
console.log(f(20,40))

//multi two numbers
var f=(num1,num2)=>num1*num2
console.log(f(10,20))

//div two numbers
var f=(num1,num2)=>num1/num2
console.log(f(100,20))

//cube
var f=(num1)=>num1**3
console.log(f(10))

//square of all numbers of array
var arr=[2,3,4,5,6,7,8,9]
var squares=arr.map(num=>num**2)
console.log(squares)

//even number
var arr=[1,2,3,4,5,6,7,8,9]
var evens=arr.filter(num=>num%2==0)
console.log(evens)

//odd number
var arr=[1,2,3,4,5,6,7,8,9]
var evens=arr.filter(num=>num%2!=0)
console.log(evens)

//ascending order
var arr=[9,1,2,7,3,8,5,4,6]
var sorted=arr.sort((num1,num2)=>num1-num2)
console.log(sorted)

//descending order
var arr=[9,1,2,7,3,8,5,4,6]
var sorted=arr.sort((num1,num2)=>num2-num1)
console.log(sorted)

//reduce
var arr=[9,1,2,7,3,8,5,4,6]
var total=arr.reduce((num1,num2)=>num1+num2)
console.log(total)

//highest value
var arr=[9,1,2,7,3,8,5,4,6]
var high=arr.reduce((num1,num2)=>num1>num2?num1:num2)
console.log(high)

//lowest or minimum value
var arr=[9,1,2,7,3,8,5,4,6]
var high=arr.reduce((num1,num2)=>num1<num2?num1:num2)
console.log(high)

