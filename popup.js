console.log("This is a popup")
console.log("This is also a popup")

function changeFont() {
    let par = document.querySelectorAll("p");
    par.forEach(element => {
        console.log(element)
    element.style.fontFamily  = "Times New Roman";
    });
}

browser.tabs.executeScript({
    code: `(${changeFont})()` //argument here is a string but function.toString() returns function's code
}, (results) => {
    //Here we have just the innerHTML and not DOM structure

});