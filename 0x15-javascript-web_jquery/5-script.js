#!/usr/bin/node
// update the content of header

$(document).ready(function()
{
    $('#update_header').click(function ()
    { 
        $('header').text("New Header!!!");
    });
});
