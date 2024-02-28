$('document').ready(function () {
  $('INPUT#btn_translate').click(my_translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (eventt) {
      if (eventt.keyCode === 13) {
        my_translate();
      }
    });
  });
});

function my_translate () {
  const my_url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(my_url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
