var _ = require("lodash");

module.exports = function(s) {
  var Walker = function() {
    this.x = this.prevx = s.int(s.random(s.width));
    this.y = this.prevy = s.int(s.random(s.height));
  };

  Walker.prototype.display = function() {
    s.stroke(0, 0, 0);
    s.line(this.prevx, this.prevy, this.x, this.y);
  };

  Walker.prototype.step = function() {
    this.prevx = this.x;
    this.prevy = this.y;
    // this.x += s.randomGaussian() * 10;
    // this.y += s.randomGaussian() * 10;
    var dist = s.random(10);
    var angle = s.random(s.TWO_PI);
    this.x += dist * s.cos(angle);
    this.y += dist * s.sin(angle);
  };

  var walkers;
  s.setup = function() {
    s.createCanvas(2*s.windowWidth, 2*s.windowHeight);
    // frameRate(60);
    s.background(255);
    walkers = _.times(100, function() {
      return new Walker();
    });
  };

  s.draw = function() {
    _.each(walkers, function(w) {
      w.step();
      w.display();
    });
  };
};
