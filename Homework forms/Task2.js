let submit = document.getElementById("submit");


function validationForm(event) {
    event.preventDefault();
    let email = document.forms["myForm"]["email"].value;
    let login = document.forms["myForm"]["login"].value;
    let password = document.forms["myForm"]["password"].value;
    let passwordRepeat = document.forms["myForm"]["passwordRepeat"].value;

    if (login === "" || email === "") {
        alert("All data must be filled out");
        return false;
    } else if (password != passwordRepeat) {
        alert("Passwords must be the same");
        return false;
    } else {
        alert("On your email, " + email + "had sent letter with confirmation form.");
    }
}

submit.addEventListener('click', validationForm)
