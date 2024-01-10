//adds a <li> element to  list when the user clicks on the tag DIV#add_item
$("#add_item").click(function(){
    $("UL.my_list").append("<li>Item</li>");
});
