document.addEventListener('DOMContentLoaded', () => {
  $('#btn_translate').click(() => {
    const valueInput = $('#language_code').val();
    const concatUrl = `https://fourtonfish.com/hellosalut/?lang=${valueInput}`;
    $.ajax({
      type: 'GET',
      url: concatUrl,
      success: (response) => {
        $('DIV p').remove();
        $('DIV#hello').append(`<p>${response.hello}</p>`);
      }
    });
  });
});
