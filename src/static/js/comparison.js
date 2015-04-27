$(function() {
  function initialize() {
    $('img').each(function(idx, img) {
      Caman(img, function() {
        this.render();
      });
    });
  }
  function render_type_change(){
    var render_type = $('input[name="render_type"]:checked').val();
    if (render_type == "normal") {
      $('canvas').each(function(idx, canvas) {
        Caman(canvas, function() {
          this.reset();
        });
      });
    } else if (render_type == "sortpixels") {
      $('canvas').each(function(idx, canvas) {
        Caman(canvas, function() {
          this.pixelsort();
          this.render();
        });
      });
    } else if (render_type == "sortpalette") {

    }
  }
  initialize();
  $('input[name="render_type"]').change(render_type_change);
  render_type_change();
});
