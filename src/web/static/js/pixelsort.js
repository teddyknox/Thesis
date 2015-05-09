// Documentation at http://camanjs.com/guides/#Extending
(function() {
  Caman.Plugin.register("pixelsort", function() {
    var pd = this.pixelData;

    pixels = [];
    for (var i = 0; i < this.pixelData.length; i+= 4) {
      var pixel = Caman.Convert.rgbToHSV(pd[i], pd[i+1], pd[i+2]);
      pixels.push(pixel);
    }
    pixels.sort(function(a, b) {
      return a.h - b.h;
    });
    pixels.forEach(function(val, idx) {
      var pixel = Caman.Convert.hsvToRGB(val.h, val.s, val.v);
      var place = idx * 4;
      pd[place] = pixel.r;
      pd[place+1] = pixel.g;
      pd[place+2] = pixel.b;
    });
  });

  // Register our filter for the plugin
  Caman.Filter.register("pixelsort", function() {
    // Here we call processPlugin so CamanJS knows how to handle it
    this.processPlugin("pixelsort", arguments);
  });
})();
