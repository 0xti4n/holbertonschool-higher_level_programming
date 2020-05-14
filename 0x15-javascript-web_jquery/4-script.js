$('DIV#toggle_header').click(function () {
  const $header = $('HEADER');
  if ($header.hasClass('green')) {
    $header.removeClass('green').addClass('red');
  } else if ($header.hasClass('red')) {
    $header.removeClass('red');
    $header.addClass('green');
  }
});
