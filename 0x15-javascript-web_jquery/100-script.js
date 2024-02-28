#!/usr/bin/node
// use javascript to change color
// Function to change the text color of the header
function changeHeaderColor() {
        document.querySelector('header').style.color = '#FF0000';
  }
  
  // Call the function when the window finishes loading
  window.onload = function() {
    changeHeaderColor();
  };