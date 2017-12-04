$(document).ready(function(){
    var data = JSON.parse(localStorage.getItem('foods'));
    console.log(data);
    var test_food1 = {
       Time: 0,
       Price: 1.4,
       Name: "PB Banana Crunch",
       restaurant: "underground"
    };
    var test_food2 ={
       Time: 1,
       Price: 4.5,
       Name: "French Toast",
       restaurant: "underground"
    };
    var test_food3 ={
       Time: 2,
       Price: 7.8,
       Name: "Mac and Cheese",
       restaurant: "underground"
    };

    var test_food4={
       Calories:"880",
       Carbohydrates: "116",
       DairyAllergy: "1",
       EggAllergy: "1",
       Fat: "38",
       FishAllergy: "0",
       HealthyChoice: "0",
       MealTime: "B",
       Name: "French Toast",
       PeanutAllery: "",
       Price: "4.5",
       Protein: "22",
       Restaurant: "underground",
       SoyAllergy: "0",
       Time: 0,
       TreenutAllergy: "0",
       Vegetarian: "1",
       WheatAllergy: "1"
    }
    //var data = [test_food4, test_food4, test_food4, test_food4, test_food4, test_food4];
    showMenu(data);
    computeTotal(data);
    // button to go back to homepage
    $("button").click(function(){
        window.location.href = "index.html";
    })

    $('.food_item').click(function(){
        var idx = Number($(this).attr("id").substring(7));
        console.log(idx);
        showFoodDetail(data[idx]);
    });
    var left = ($(document).width() - $('#windows').width())  /2;
    $('#windows').css({left:left});
    $("#mybg").hide();
    $("#windows").hide();
    $("#mybg").click(function () {
        $("#windows").hide();
        $(this).hide();
    })
});

function showMenu(data){
    // find the table element
    var num_row = 1;
    var weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    var counts = [0,0,0];
    for(i = 0 ; i < data.length; i++){
        var food = data[i];
        //console.log(food);
        var nth = counts[food["Time"]];
        var row = $('#menu1 tbody tr:last');
        //console.log(row);
        if(nth >= num_row){
            //console.log("NEED A NEW ROW !");
            // add another row and insert
            row.parent().append("<tr></tr>")
            row = $('#menu1 tr:last');
            //console.log(row);
            for(var j =0; j < 4;j++){
                if(j == 0)
                    row.append("<td>" + weekdays[num_row] + "</td>");
                else
                    row.append("<td class='food_item' ></td>");
            }
            num_row++;
        }else{
            //console.log("NO NEED ");
        }
        // change the content
        var selector = "#menu1 tbody tr:nth-child(" + (counts[food["Time"]] +1) + ") td:nth-child(" + (food["Time"]+2)+")";
        //console.log(selector);
        var elem = $(selector);
        elem.attr("id", 'food_id' + i);
        //console.log(elem)
        elem.text(food["Name"] + " ($" + food["Price"] + ")");
        counts[food["Time"]]++;
    }
}

function computeTotal(data){
    var total_calories = 0;
    var total_protein = 0;
    var total_fat = 0;
    var total_carb = 0;
    for(i=0;i<data.length;i++){
        total_calories += Number(data[i]["Calories"]);
        total_protein += Number(data[i]["Protein"]);
        total_fat += Number(data[i]["Fat"]);
        total_carb += Number(data[i]["Carbohydrates"]);
    }
    //menu tds
    var row = $("#energy tr:nth-child(1) td");
    row.eq(1).html(total_calories);
    row.eq(2).html(total_protein);
    row.eq(3).html(total_fat);
    row.eq(4).html(total_carb);
}

function showFoodDetail(food){
    $("#food_name").html(food["Name"]);
    $("#food_restaurant").html(food["Restaurant"]);
    $("#food_fat").html(food["Fat"]);
    $("#food_protein").html(food["Protein"]);
    $("#food_calorie").html(food["Calories"]);
    $("#food_carb").html(food["Carbohydrates"]);
    $("#food_price").html(food["Price"]);
    $("#windows").show();
    $('#mybg').show().height( $(document).height() ).css({'opacity':0.7});
}