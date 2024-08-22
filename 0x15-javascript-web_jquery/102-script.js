$(document).ready(() => {
  $('#btn_translate').click(() => {
    const langCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
