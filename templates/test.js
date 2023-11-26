// window.onload = function () {
//     onload_window_zmina = document.getElementById("zmina")
//     console.log(onload_window_zmina)
//     onload_window_zmina.innerHTML = "<h1>Hello world!!!!</h1>"
// }

window.onload = function () {
    let onload_window_zmina = document.getElementById("zmina");
    let age = prompt("Скільки тобі років");
    let years = age * 2;
    let result = "Число: " + years;
    onload_window_zmina.innerHTML = result;
}
