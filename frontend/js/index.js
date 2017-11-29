$(document).ready(function () {
    $("p").click(function(){
        $(this).hide();
        console.log("I hide it");
    });

    $("form").submit(function (e) {
        console.log("on submit");
        e.preventDefault();
        sendUserData();
    });
    $("#op-gender").click(function () {
        var temp = $(this).text();
        $(this).text($("#gender").text());
        $("#gender").html(temp + "\n<span class=\"caret\"></span>");
    })
});

function sendUserData(){
    console.log("in send user data");
    // get height
    var height = Number($("#height").val());
    var weight = Number($("#weight").val());
    var age = Number($("#age").val());
    var gender = $("#gender").text().trim();
    var data= new Object();
    data.height = height;
    data.weight = weight;
    data.age = age;
    data.gender = gender;
    console.log(data);
    var str = JSON.stringify(data);
    console.log(str);
    // post json to server
    $.ajax({
        url: '/calculate',
        type: 'POST',
        contentType: 'application/json',
        data: str,
        dataType: 'json',
        success: function(foods){
            console.log(foods);
            console.log(typeof foods)
            localStorage.setItem("foods", JSON.stringify(foods));
            window.location.href = "menu.html";
        }
    });

    //test
    // var foods = "hello";
    // console.log(foods);
    // localStorage.setItem("foods", foods);
    // window.location.href = "menu.html";
   // alert("json posted!");
};