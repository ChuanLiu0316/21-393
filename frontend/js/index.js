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

    $("form input:text").focusout(function(){
        var input = $(this).val();
        var word = "<strong>Oops.</strong> Please enter a valid number.";
        if(isNaN(input)){
            $(this).next().html(word);
        }else{
            $(this).next().html("");
        }
    });

    var slider = document.getElementById("myRange");
    var output = document.getElementById("activity_level");
    output.innerHTML = (1.2+ (slider.value /100)*0.7).toFixed(2); // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
        output.innerHTML = (1.2+(this.value/100)*0.7).toFixed(2);
    }

});


function sendUserData(){
    console.log("in send user data");
    // get height
    var height = Number($("#height").val());
    var weight = Number($("#weight").val());
    var age = Number($("#age").val());
    var gender = $("#gender").text().trim().toLowerCase();
    // get allergy list
    var allergies = [];
    var checkbox = $("input[type='checkbox']:checked");
    for(i =0; i < checkbox.length; i++){
        allergies.push(checkbox.eq(i).val());
    }
    var data= new Object();
    data.height = height;
    data.weight = weight;
    data.age = age;
    data.gender = gender; // "male" "female"
    data.allergy = allergies;
    data.activity = Number((1+$("#myRange").val()/100).toFixed(2)); // set activity level
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
            localStorage.setItem("calories",
                Math.round(5*computeCalories(data.weight,
                    data.height, data.age,data.gender,data.activity)));
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

function computeCalories(weight, height, age, gender, activity){
    var BMR;
    if(gender=="male"){
       BMR = 66.5+(13.75*weight)+(5.003*height)-(6.755*age);
    }else{
        BMR = 655.1+(9.563*weight)+(1.850*height)-(4.676*age);
    }
    return activity*BMR;
}