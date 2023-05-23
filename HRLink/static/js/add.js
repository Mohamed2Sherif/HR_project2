const form = document.querySelector('form');

form.addEventListener('submit', function(e){
  e.preventDefault();
  // Get employees
  var empolyees = JSON.parse(localStorage.getItem('empolyees'));
  // if empty
  if (empolyees == null){
    empolyees = [];
  }
  // get gender
  function getGender(){
    if (document.getElementById('male').checked){
        return 'male';
    }
    else{
      return 'female';
    }
  }
  //create an object
  const empolyee = {
    name: document.getElementById('name').value,
    id: document.getElementById('id').value,
    email: document.getElementById('email').value,
    address: document.getElementById('address').value,
    phone: document.getElementById('phone').value,
    gender: getGender(),
    availableVac: document.getElementById('availableVac').value,
    actualVac: document.getElementById('actualVac').value,
    salary: document.getElementById('salary').value,
    birthDate: document.getElementById('birthDate').value,
  }
  empolyees.push(empolyee);
  localStorage.setItem("empolyees", JSON.stringify(empolyees));
  location.reload();
  // try {            
  //   empolyees.push(empolyee);
  //   localStorage.setItem("empolyees", JSON.stringify(empolyees));
  //   alert("The data is saved");
  //   return true;          
  // }
  // catch (e) {
  //   if (e == QUOTA_EXCEEDED_ERR) {
  //    alert('Quota exceeded!');
  //   }
  // }
})






// function addEmp() {
//     location.replace("Add.html")
//   }
//   arr = [document.getElementById("update") , document.getElementById("delete") , document.getElementById("search") , document.getElementById("vacationRequest")]
//   function openForm(x) {
//     x--
//     for(i = 0  ; i < 4 ; i++){
//         if(i != x){
//           arr[i].style.display = "none"
//         }else{
//           arr[i].style.display = "block"
//         }
//      }
//   }
//   function Close(){
//     for(i = 0  ; i < 4 ; i++){
//           arr[i].style.display = "none"
//      }
//   }
