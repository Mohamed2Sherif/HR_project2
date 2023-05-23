var empolyees = JSON.parse(localStorage.getItem('empolyees'));
// if empty
if (empolyees == null){
    empolyees = [];
}
var table = document.getElementById('table');
var tableData = document.getElementsByTagName('td');
var tableRows = document.getElementsByTagName('tr');
for (empolyee of empolyees) {
    let template = 
                `<tr>
                    <td>${empolyee.id}</td>
                    <td>${empolyee.name}</td>
                    <td>${empolyee.email}</td>
                    <td>${empolyee.address}</td>
                    <td>${empolyee.phone}</td>
                    <td>${empolyee.gender}</td>
                    <td>${empolyee.availableVac}</td>
                    <td>${empolyee.actualVac}</td>
                    <td>${empolyee.salary}</td>
                    <td>${empolyee.birthDate}</td>
                    <td><button id="update${empolyees.indexOf(empolyee)}">update</button></td>
                    <td><button id="delete${empolyees.indexOf(empolyee)}">delete</button></td>
                </tr>`;
    
    table.innerHTML += template;
}
// update action
for (let i = 0; i < empolyees.length; i++) {
    var btn = document.getElementById(`update${i}`);
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        localStorage.setItem('autoFill',JSON.stringify(empolyees[i]));
        window.open('update.html');
    })
}
// delete action
for (let i = 0; i < empolyees.length; i++) {
    var btn = document.getElementById(`delete${i}`);
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        empolyees.splice(i, 1);
        localStorage.setItem('empolyees',JSON.stringify(empolyees));
        location.reload();
    })
}
// function deleteEmpolyee(idx){
//     console.log(idx);
//     empolyees = empolyees.splice(idx, 1);
//     localStorage.setItem('empolyees', JSON.stringify(empolyees));
//     location.reload();
// }
