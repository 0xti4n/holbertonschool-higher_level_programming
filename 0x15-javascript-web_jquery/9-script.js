$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (response) => {
      $('DIV#hello').append(response.hello);
    }
  });
});
