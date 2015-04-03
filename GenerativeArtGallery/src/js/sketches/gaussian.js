module.exports = function(s) {

  s.setup = function() {
    s.createCanvas(s.windowWidth, s.windowHeight);
    s.frameRate(60);
  }

  s.draw = function() {
    var num = s.randomGaussian();
    var sd = 60;
    var mean = 320;

    // Multiply by the standard deviation and add the mean.
    var x = sd * num + mean;

    s.noStroke();
    s.fill(255,10);
    s.ellipse(x, 180, 16, 16);
  }
};
