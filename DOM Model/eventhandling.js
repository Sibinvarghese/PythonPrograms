let clk=document.querySelector("#clk")

function clkedfn(){
    clk.style.color="red";
    clkedfn.textContent="Clicked On Me"
}
clk.addEventListener("click",clkedfn)


let dbl=document.getElementById("dbl")
dbl.addEventListener("dblclick",()=>{
    dbl.style.color="green";
    dbl.textContent="dbclicked";
})

let hov=document.querySelector("#hov")
hov.addEventListener("mouseover",()=>{
    hov.textContent="Mouse Over Me"
 hov.style.color="cyan"
})

hov.addEventListener("mouseout",()=>{
    hov.textContent="Mouse Not Over Me";
    hov.style.color="red"
})