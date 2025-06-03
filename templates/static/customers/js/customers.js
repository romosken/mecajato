function add_car() {
  container = document.getElementById("form-carro");

  html =
    "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='Car Model' class='form-control' name='car-model'></div> <div class='col-md'><input type='text' placeholder='Car Plate' class='form-control' name='car-plate'> </div><div class='col-md'><input type='number' placeholder='Car Year' class='form-control' name='car-year'> </div></div>";

  container.innerHTML += html;
}
