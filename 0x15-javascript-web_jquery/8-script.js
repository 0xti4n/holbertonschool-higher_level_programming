$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: (response) => {
      response.results.forEach(element => {
        const content = '<li>' + element.title + '</li>';
        $('UL#list_movies').append(content);
      });
    }
  });
});
