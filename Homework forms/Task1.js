let submit = document.getElementById("submit");


function validationForm(event) {
    event.preventDefault();
    let login = document.forms["myForm"]["login"].value;
    let password = document.forms["myForm"]["password"].value;
    let checkbox = document.forms["myForm"]["checkbox"];

    if (login === "") {
        alert("Login must be filled out");
        return false;
    } else if (password === "") {
        alert("Password must be filled out");
        return false;
    } else if (checkbox.checked) {
        alert("Hello, " + login + "! I remember you");
    } else {
        alert("Hello, " + login + "! I don't remember you");
    }
}

submit.addEventListener('click', validationForm)
