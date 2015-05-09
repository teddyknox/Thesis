Caman.Plugin.register("palettesort", function() {
  var canvas = document.createElement('canvas');
  canvas.width = width;
  canvas.height = height;

  // Get the new context and draw a portion of the current canvas
  // to the new canvas.
  ctx = canvas.getContext('2d');
  ctx.drawImage(this.canvas, x, y, width, height, 0, 0, width, height);

  // Tell CamanJS to replace the current canvas with our new cropped one.
  this.replaceCanvas(canvas);
});

// Register our filter for the plugin
Caman.Filter.register("palettesort", function() {
  // Here we call processPlugin so CamanJS knows how to handle it
  this.processPlugin("palettesort", arguments);
});
