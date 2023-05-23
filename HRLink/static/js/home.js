var empolyees = JSON.parse(localStorage.getItem('empolyees'));

// update
updateBtn = document.getElementById('updateBtn');
updateBtn.addEventListener('click', function(e){
    e.preventDefault();
    var value = document.getElementById("employeeId1").value;
    for (let i = 0; i < empolyees.length; i++) {
        if (empolyees[i].id == value){
            localStorage.setItem('autoFill',JSON.stringify(empolyees[i]));
            window.open('update.html');
        }
    }
})

// delete
deleteBtn = document.getElementById('deleteBtn');
deleteBtn.addEventListener('click', function(e) {
    e.preventDefault();
    var value = document.getElementById("employeeId2").value;
    for (let i = 0; i < empolyees.length; i++) {
        if (empolyees[i].id == value){
            empolyees.splice(i, 1);
            localStorage.setItem('empolyees', JSON.stringify(empolyees));
        }
    }
    location.reload();
})

// search
searchBtn = document.getElementById('searchBtn');
searchBtn.addEventListener('click', function(e){
    e.preventDefault();
    var value = document.getElementById("employeeName").value;
    // new array
    var secEmpolyees = [];
    // if empty
    for (let i = 0; i < empolyees.length; i++) {
        // generate substrings
        for (let j = 0; j < empolyees[i].name.length; j++){
            let newStr = "";
            for (let k = j; k < empolyees[i].name.length && newStr.length < value.length; k++){
                newStr += empolyees[i].name[k];
            }
            if (newStr.toLocaleLowerCase() === value.toLocaleLowerCase()){
                secEmpolyees.push(empolyees[i]);
                break;
            }
        }
    }
    localStorage.setItem("secEmpolyees", JSON.stringify(secEmpolyees));
    window.open("secTable.html");
})