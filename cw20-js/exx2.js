let age = prompt("Enter age");
// let toint=parseInt(userinput,10);

if (age>0 && age <10){
    console.log("it's child")
}else if(age>11 && age<18) {
    console.log("it's teen")
}else if(age>19 && age<30) {
    console.log("it's young")
}else{
    console.log("it's adult")
}
