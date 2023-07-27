function createTable() {
    let table = document.createElement("table");

    let data = [
        {
            label: "Firstname",
            name: "firstname"
        },
        {
            label: "Lastname",
            name: "lastname"
        },
        {
            label: "Birthday",
            name: "birthday"
        },
        {
            label: "Gender",
            name: "gender"
        },
        {
            label: "Country",
            name: "country"
        },
        {
            label: "City",
            name: "city"
        },
        {
            label: "Skills",
            name: "skills"
        }
    ];

    data.forEach(function (data) {
        let row = document.createElement("tr");
        let labelCell = document.createElement("td");
        let valueCell = document.createElement("td");
        labelCell.textContent = data.label;

        if (data.name === "skills") {
            let skills = document.forms["myForm"][data.name];
            let selectedSkills = [];
            for (let i = 0; i < skills.length; i++) {
                if (skills[i].checked) {
                    selectedSkills.push(skills[i].value);
                }
            }
            valueCell.textContent = selectedSkills.join(", ");
        } else {
            valueCell.textContent = document.forms["myForm"][data.name].value;
        }

        row.appendChild(labelCell);
        row.appendChild(valueCell);
        table.appendChild(row);
    });

    return table;
}
let container = document.querySelector(".container");

function contain() {
    let table = document.createElement("table");
    table.appendChild(createTable());
    container.appendChild(table);
}

function validationForm(event) {
    event.preventDefault();

    let firstname = document.forms["myForm"]["firstname"].value;
    let lastname = document.forms["myForm"]["lastname"].value;
    let checkbox = document.forms["myForm"]["skills"].value;

    if (firstname === "" || lastname === "") {
        alert("All input must be filled out");
        return false;
    } else {
        contain();
    }
}

document.forms["myForm"].addEventListener("submit", validationForm);
