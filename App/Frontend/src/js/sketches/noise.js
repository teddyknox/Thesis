module.exports = function(s) {
  s.setup = function() {
    s.createCanvas(s.windowWidth, s.windowHeight);
    s.noiseDetail(12);
    s.background(34, 47, 121);
  };

  s.draw = function() {
    s.loadPixels();
    for (var y = 0; y < s.height; y += 1) {
      for(var x = 0; x < s.width; x += 1) {
        var loc = (s.width * y + x) * 4;
        var nx = s.map(x, 0, s.width, 0, 5);
        var ny = s.map(y, 0, s.height, 0, 5);
        var alpha = Math.round(s.noise(nx, ny) * 100) + 155;
        // s.pixels[loc] = 0;
        // s.pixels[loc + 1] = 0;
        // s.pixels[loc + 2] = 0;
        s.pixels[loc + 3] = alpha;
      }
    }
    s.updatePixels();
    s.noLoop();
  };
};
