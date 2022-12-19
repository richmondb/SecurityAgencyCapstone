// disable video on website right click
var video = document.querySelectorAll('video');

video.forEach(element => {
    // Now do something with my button
    element.setAttribute('oncontextmenu', "return false;");
});


// get div name
let box = document.querySelector("header");
// get element by id
let e = document.getElementById("sec_1");
// get div width and height
// let width = box.offsetWidth;
let width = screen.width;
let height = box.offsetHeight;
// set height via js
if (width > 992) {
    e.style.height = "calc(100vh - " + height + "px)";
}
//  remove for production
console.log({ height });
console.log({ width });
