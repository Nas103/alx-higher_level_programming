$(document).ready(() => {
  function translate() {
    const langCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translate);
  $('#language_code').keypress((e) => {
    if (e.which === 13) {
      translate();
    }
  });
});
