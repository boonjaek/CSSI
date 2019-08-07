function setPicture() {
    var carDropDown = document.getElementById("carType");
    var value = carDropDown.options[carDropDown.selectedIndex].value;
    var img = document.getElementById("currentImage");
    // alert(value);
    img.src = value;
}

// function carAge() {
//   var carMileage = document.getElementById("Mileage").value;
//   var age = ((carMileage/200000)*80.3);
//   return age
// }
