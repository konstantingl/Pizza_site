document.addEventListener('DOMContentLoaded', function() {

document.querySelectorAll('table input').forEach(function(input) {

  // Details block appear
  input.onclick = () => {
    // document.querySelector('#large_size').style.display = "none";
    let inputData = input.name.split(',', 2);
    localStorage.setItem('the_name', inputData[0]);
    var category = inputData[1];
    console.log(inputData);
    document.querySelector('#large_size').setAttribute("disabled", false);
    if (category=='Regular Pizza' || category=='Sicilian Pizza'){
      document.querySelector('.toppings').style.display = "flex";
      document.querySelector('.extras').style.display = "none";
      document.querySelector('#large_size').removeAttribute("disabled");
    }
    else if (category=='Sub'){
      document.querySelector('.extras').style.display = "flex";
      document.querySelector('.toppings').style.display = "none";
      document.querySelector('#large_size').removeAttribute("disabled");
    }
    else if (category=='Salad' || category=='Pasta'){
      document.querySelector('#large_size').setAttribute("disabled", true);
    }
    else if (category=='Dinner'){
      document.querySelector('#large_size').removeAttribute("disabled");
    }
    document.querySelector('#details_block').style.display = "block";
    document.querySelector('#overlay').style.display = "flex";
    return false;
  };
  });
});

// Details block disappear
function off(){
  document.querySelector('#details_block').style.display = "none";
  document.querySelector('#overlay').style.display = "none";
  return false;
};


document.addEventListener('DOMContentLoaded', function() {

document.querySelector('#details_form').onsubmit = () => {

  // Send request with selection to server
  let request = new XMLHttpRequest();

  name = localStorage.getItem('the_name');
  var form = new FormData();
  form.append('product_selected', name);
  console.log(name);
  let size = document.querySelector('#size_select').value;
  form.append('size', size);

  // Count toppings
  var toppings = [];
  var x = document.querySelectorAll('.tops_select');
  for (var i=0; i < x.length; i++) {
    if (x[i].checked){
      toppings.push(x[i].value);
    }
  };

  var extras = [];
  var x = document.querySelectorAll('.extra_select');
  for (var i=0; i < x.length; i++) {
    if (x[i].checked){
      extras.push(x[i].value);
    }
  };

  // Check amount of toppings allowed
  let error = 'Too many toppings selected';
  if (name == 'Cheese Regular' && toppings.length > 0){
      document.querySelector('#details_error').innerHTML = error;
      return false;
  }
  else if ((name == '1 topping' || name == '1 item') && toppings.length > 1) {
      document.querySelector('#details_error').innerHTML = error;
      return false;
  }
  else if ((name == '2 toppings' || name == '2 items') && toppings.length > 2) {
      document.querySelector('#details_error').innerHTML = error;
      return false;
  }
  else if ((name == '3 toppings' || name == '3 items') && toppings.length > 3) {
      document.querySelector('#details_error').innerHTML = error;
      return false;
  }
  else {
      document.querySelector('#details_error').innerHTML = '';
  }


  form.append('tops_selected', toppings);
  form.append('extra_selected', extras);


  request.open('POST', 'update_cart');
  var csrfCookie = document.cookie.split('=');
  if (csrfCookie) {
    request.setRequestHeader("X-CSRFToken", csrfCookie[1]);
    }
  request.send(form);
};
});
