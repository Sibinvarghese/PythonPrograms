class MyBank{

    static getUserData(){
        var users={
            userone:{username:"userone",password:"userone",acno:1000,balance:25000},
            usertwo:{username:"usertwo",password:"usertwo",acno:1001,balance:20000},
            userthree:{username:"userthree",password:"userthree",acno:1002,balance:23000},
        }
        return users

    }

    static Login(){
        let uname=document.querySelector("#uname").value
        let password=document.querySelector("#pwd").value
//        alert(uname+","+password)
        let users=MyBank.getUserData()
        if(uname in users){
            if(password==users[uname]["password"]){
                window.location.href="UserHome.html"
                alert(" Login Success")
            }
            else{
                alert("Invalid Password")
            }
        }
        else{
            alert("Their is no user")
        }
    }
    static deposit(){
        let uname=document.querySelector("#uname").value
        let amt=Number(document.querySelector("#amount").value)
//        alert(uname+","+amt)
        var users=MyBank.getUserData()
        if(uname in users){
            users[uname]["balance"]+=amt
            alert(users[uname]["balance"])
        }
        else{
            alert("invalid username")
        }
    }
    static withdraw(){
      let uname=document.querySelector("#uname").value
        let amt=Number(document.querySelector("#amount").value)
//        alert(uname+","+amt)
        var users=MyBank.getUserData()
        if(uname in users){
            if(amt>users[uname]["balance"]){
                alert("Insufficient Balance")
            }
            else{
                users[uname]["balance"]-=amt
                alert(users[uname]["balance"])

            }
        }
        else{
            alert("invalid username")
        }



    }


}