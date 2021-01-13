
let employee=[
		{eid:100,name:"ajay",desig:"devop",join:1981,resign:2003},
		{eid:101,name:"vijay",desig:"devop",join:1992,resign:2008},
		{eid:102,name:"bijoy",desig:"ba",join:1999,resign:2007},
		{eid:103,name:"jhon",desig:"ba",join:1989,resign:2010},
		{eid:104,name:"danie",desig:"qa",join:2009,resign:2014},
		{eid:105,name:"lari",desig:"qa",join:1987,resign:2010},
		]

	//qs1: print all employee name and designation only
	for(let emp of employee){
	console.log(emp.name+','+emp.desig)
	}

	//qs2:print all employee details whose desig equals devop
	var employees=employee.filter(emp=>emp.desig=="devop")
	console.log(employees)

	//qs3:print all employee details those who are woking in 80s  [*(>1980 & <1190)]
    var f=employee.filter(num=>(num.join>=1980 & num.join<1990))
    console.log(f)
	//qs4:print all employee details those who have experience >9 years
	var v=employee.filter(abc=>abc.resign-abc.join>9)
	console.log(v)
	//qs5:sort all employees based on their joining year
	var s=employee.sort((val1,val2)=>val1.join>val2.join?1:-1)
	console.log(s)

