#!/usr/bin/node
// frtch all taitles



$(document).ready(function(){
    // Fetch movies data from the API
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status){
      // Check if the request was successful
      if(status === "success") {
        // Loop through each movie in the data
        $.each(data.results, function(index, movie){
          // Append a new list item with the movie title to UL#list_movies
          $("#list_movies").append("<li>" + movie.title + "</li>");
        });
      } else {
        // If request fails, display an error message
        $("#list_movies").append("<li>Error fetching movies</li>");
      }
    });
  });