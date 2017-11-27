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
});

function sendUserData(){
    console.log("in send user data");
    // get height
    var height = Number($("#height").val());
    var weight = Number($("#weight").val());
    var age = Number($("#age").val());
    var gender = $("#gender").val();
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
        url: '/localhost:5000',
        type: 'POST',
        contentType: 'application/json',
        data: str,
        dataType: 'json',
        success: function(data){
            console.log(data);
        }
    });
    alert("json posted!");
};