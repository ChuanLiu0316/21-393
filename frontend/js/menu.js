$(document).ready(function(){
   var data = JSON.parse(localStorage.getItem('foods'));
   console.log(data);
   var test_food1 = {
       time: 0,
       price: 1.4,
       name: "PB Banana Crunch",
       restaurant: "underground"
   };
   var test_food2 ={
       time: 1,
       price: 4.5,
       name: "French Toast",
       restaurant: "underground"
   };
   var test_food3 ={
       time: 2,
       price: 7.8,
       name: "Mac and Cheese",
       restaurant: "underground"
    };
   var testdata = [test_food1, test_food2, test_food3, test_food1, test_food2, test_food3];
   showMenu(data);
   //showMenu(testdata);

   // button to go back to homepage
    $("button").click(function(){
        window.location.href = "index.html";
    })

    $('.food_item').click(function(){

    });

});

function showMenu(data){
    // find the table element
    var num_row = 1;
    var weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    var counts = [0,0,0];
    for(i = 0 ; i < data.length; i++){
        var food = data[i];
        console.log(food);
        var nth = counts[food["time"]];
        var row = $('#menu1 tbody tr:last');
        console.log(row);
        if(nth >= num_row){
            console.log("NEED A NEW ROW !");
            // add another row and insert
            row.parent().append("<tr></tr>")
            row = $('#menu1 tr:last');
            console.log(row);
            for(var j =0; j < 4;j++){
                if(j == 0)
                    row.append("<td>" + weekdays[num_row] + "</td>");
                else
                    row.append("<td class='food_item'></td>");
            }
            num_row++;
        }else{
            console.log("NO NEED ");
        }
        // change the content
        var selector = "#menu1 tbody tr:nth-child(" + (counts[food["time"]] +1) + ") td:nth-child(" + (food["time"]+2)+")";
        console.log(selector);
        var elem = $(selector);
        console.log(elem)
        elem.text(food["name"] + " ($" + food["price"] + ")");
        counts[food["time"]]++;
    }
}

function showFoodDetail(food){

    var html ='<div id="windows">' +
        ' </div><div id="bg"></div>';
    $('body').append(html);
    var left = ($(document).width() - $('#windows').width())  /2;
    $('#windows').css({left:left});
    $('#bg').show().height( $(document).height() ).css({'opacity':0.7});
}