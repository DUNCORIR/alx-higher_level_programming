$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/?callback=?', { lang }, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error fetching translation');
    });
  });
});
