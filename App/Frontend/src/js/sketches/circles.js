module.exports = function(s) {
  s.setup = function() {
    s.createCanvas(s.windowWidth, s.windowHeight);
    s.frameRate(60);
    s.background(255);
    s.noLoop();
  };

  var t = 0.0;

  s.draw = function() {
    var n = s.noise(t);
    t += 0.01;
    var x = s.map(n, 0, 1, 0, 400);

    s.background(255);
    s.stroke(0);
    s.fill(0);
    s.ellipse(s.width/2, s.height/2, x, x);
  };
};
