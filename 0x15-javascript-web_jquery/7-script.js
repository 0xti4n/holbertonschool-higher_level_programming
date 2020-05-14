$(function () {
  const $name = $('DIV#character');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function (response) {
      $name.append(response.name);
    }
  });
});
