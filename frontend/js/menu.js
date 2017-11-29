$(document).ready(function(){
   var data = JSON.parse(localStorage.getItem('foods'));
   console.log(data);
   condole.log(typeof data);
});