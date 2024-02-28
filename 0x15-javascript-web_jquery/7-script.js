#!/usr/bin/node
// fetch name

$(document).ready(function(){
      // Make an AJAX request to fetch name
      $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data, status){
        // Display the fetched name in a span element
        $("#character").text(data.name);
      });
  });