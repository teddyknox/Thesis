$(function() {
  function nextImage() {
    $.get('image').then(function(url) {
      $('#canvas').attr('src', url);
    });
  }
  function pretty() {
    $.post($('#canvas').attr('src'), {label: 1}, nextImage);
  }
  function ugly() {
    $.post($('#canvas').attr('src'), {label: 0}, nextImage);
  }
  nextImage();
  $('#pretty').click(pretty);
  $('#ugly').click(ugly);
  $('body').keydown(function(e) {
    if (e.keyCode == 80) {
      var event = new MouseEvent('click', {
        'view': window,
        'bubbles': true,
        'cancelable': true
      });
      $('#pretty').trigger(event);
    } else if (e.keyCode == 85) {
      var event = new MouseEvent('click', {
        'view': window,
        'bubbles': true,
        'cancelable': true
      });
      $('#ugly').trigger(event);
    }
  });
});
