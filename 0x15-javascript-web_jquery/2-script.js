#!/usr/bin/node
//script that updates the text color of the <header> element to red (#FF0000):

$(document).ready(function()
{
    $('#red_header').click(function()
    {
        $('header').css('color','#FF0000')
    });
});