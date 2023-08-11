let userinput = prompt("Enter something");
let userinputtype=parseInt(userinput,10)

if (isNaN(userinputtype)){
    console.log('String')

}else {
console.log(`type of what you entered: ${typeof userinputtype}`)
}