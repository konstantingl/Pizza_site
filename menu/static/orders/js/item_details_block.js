document.addEventListener('DOMContentLoaded', function() {

document.querySelectorAll('table input').forEach(function(input) {

  // Details block appear
  input.onclick = () => {
    localStorage.setItem('choise', input.name);
    console.log(localStorage.choise);
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

  // console.log(document.cookie);
  var form = new FormData();
  form.append('product_selected', localStorage.choise);
  let size = document.querySelector('#size_select').value;
  form.append('size', size);

  var toppings = [];
  var x = document.querySelectorAll('.tops_select');
  for (var i=0; i < x.length; i++) {
    if (x[i].checked){
      toppings.push(x[i].value);
    }
  };
  form.append('tops_selected', toppings);
console.log(form);

  request.open('POST', 'update_cart');
  var csrfCookie = document.cookie.split('=');
  console.log(csrfCookie[1]);
  if (csrfCookie) {
    request.setRequestHeader("X-CSRFToken", csrfCookie[1]);
    }
  request.send(form);
};
});
