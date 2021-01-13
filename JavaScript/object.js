person={name:"Sibin",age:25,salary:25000}

console.log(person)      // print all values

console.log(person["name"])  //print the name

console.log(person["salary"])  //print the salary
console.log(person.salary)  //print the salary

person["salary"]+=5000      //udpate the salary
console.log(person.salary)
//OR
console.log(person["salary"]+5000)  //udpate the salary
console.log(person.salary+5000)   //udpate the salary

console.log("gender" in person)   //checking the gender in this person

person.gender="male"
console.log(person)   // adding key and their values
//OR
console.log(person.gender="male")   // adding key and their values
console.log(person )
