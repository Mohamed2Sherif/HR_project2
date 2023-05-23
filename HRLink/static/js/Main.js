function addEmp() {
    location.replace("Add.html")
  }
  arr = [document.getElementById("update") , document.getElementById("delete") , document.getElementById("search") , document.getElementById("vacationRequest")]
  function openForm(x) {
    x--
    for(i = 0  ; i < 4 ; i++){
        if(i != x){
          arr[i].style.display = "none"
        }else{
          arr[i].style.display = "block"
        }
     }
  }
  function Close(){
    for(i = 0  ; i < 4 ; i++){
          arr[i].style.display = "none"
     }
  }
