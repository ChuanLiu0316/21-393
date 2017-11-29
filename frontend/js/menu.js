$(document).ready(function(){
   var data = JSON.parse(localStorage.getItem('foods'));
   console.log(data);
   console.log(typeof data);
});