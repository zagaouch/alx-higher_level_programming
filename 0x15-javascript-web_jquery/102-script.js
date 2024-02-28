#!/sur/bin/node
//  hello  

$(document).ready(function(){
    $('#btn_translate').click(function(){
      var languageCode = $('#language_code').val();
      
      // Make AJAX request to fetch translation
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        method: 'GET',
        data: { lang: languageCode },
        success: function(response) {
          $('#hello').text(response.hello);
        },
        error: function() {
          $('#hello').text('Translation not available');
        }
      });
    });
  });
  