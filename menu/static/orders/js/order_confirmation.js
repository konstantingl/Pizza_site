document.addEventListener('DOMContentLoaded', function() {
// $('.trigger').css("display","none");
$('#order_confirm').click(function(){
  $('#overlay_cart').css("display","flex");
  $('#details_block').css("display","block");
});

$('#place_order').click(function(){
  $('svg').css('display','inline');
  setTimeout(function(){
    $(".trigger").toggleClass("drawn");
  },
  1000);
  setTimeout(function(){
    window.location.href = '/';},
  4000);
  return false;

});
});

function off(){
  document.querySelector('#details_block').style.display = "none";
  document.querySelector('#overlay_cart').style.display = "none";
  return false;
};
