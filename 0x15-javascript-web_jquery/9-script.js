#!/usr/bin/node
// display hello

$(document).ready(function () {
    $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr",
        function (data, status) {
            $('#hello').text(data.hello)
        }
    );
});