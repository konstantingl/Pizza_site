document.addEventListener("DOMContentLoaded", () => {

menu_button = document.querySelector('#menu_switch1');
cart_button = document.querySelector('#menu_switch2');

cart_button.onclick = () => {

  cart_button.className = 'active';
  menu_button.className = 'inactive';
};

menu_button.onclick = () => {

  cart_button.className = 'inactive';
  menu_button.className = 'active';
};
});
