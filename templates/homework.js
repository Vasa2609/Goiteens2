window.onload = function () {
    let onload_window_zmina = document.getElementById("zmina");
    let username = prompt("введи ім'я");
    let password = username * 3;
    let result = "Число: " * password;
    onload_window_zmina.innerHTML = result;
}
