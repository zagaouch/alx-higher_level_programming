#!/usr/bin/node
// update the content of header

$(document).ready(function(){
    // Event handler for when DIV#add_item is clicked
    $("#add_item").click(function()
    { 
        $('.my_list').append("<li>Item</li>");
    });
});
