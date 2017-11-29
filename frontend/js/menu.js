$(document).ready(function(){
   //var data = JSON.parse(localStorage.getItem('foods'));
   //console.log(data);
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
   var testdata = [test_food1, test_food2, test_food3];
   showMenu(testdata);

   // button to go back to homepage
    $("button").click(function(){
        window.location.href = "index.html";
    })

});

function showMenu(data){
    // find the table element
    var num_row = 1;

    var counts = [0,0,0];
    for(i = 0 ; i < data.length; i++){
        var food = data[i];
        console.log(food);
        var nth = counts[food["time"]];
        var row = $('#menu tbody tr:last');
        console.log(row);
        if(nth >= num_row){
            console.log("NEED A NEW ROW !");
            // add another row and insert
            row.parent().append("<tr></tr>")
            row = $('#menu tr:last');
            for(var j =0; j < 3;j++){
                row.append("<td></td>");
            }
            num_row++;
        }else{
            console.log("NO NEED ");
        }
        // change the content
        var selector = "#menu tbody tr:nth-child(" + (counts[food["time"]] +1) + ") td:nth-child(" + (food["time"]+1)+")";
        console.log(selector);
        var elem = $(selector);
        console.log(elem)
        elem.text(food["name"] + " ($" + food["price"] + ")");
        counts[food["time"]]++;
    }
}