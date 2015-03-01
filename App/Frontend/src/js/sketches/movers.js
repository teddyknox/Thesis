module.exports = function(s) {
  var movers = [];

  var Mover = function() {
    this.location = s.createVector(s.random(s.width), s.random(s.height));
    this.velocity = s.createVector(0, 0);
    this.topspeed = 4;
  };

  Mover.prototype.update = function() {
    var mouse = s.createVector(s.mouseX, s.mouseY);
    var dir = mouse.sub(this.location);
    // var pull = 1/dir.magSq();
    var acceleration = dir.normalize();
    this.velocity.add(acceleration);
    this.location.add(this.velocity);
  };

  Mover.prototype.display = function() {
    s.stroke(0);
    s.fill(175);
    s.ellipse(this.location.x, this.location.y, 16, 16);
  };

  s.setup = function() {
    s.createCanvas(s.windowWidth, s.windowHeight);
    // s.frameRate(60);
    for (var x = 0; x < 10; x += 1) {
      movers[x] = new Mover();
    }
    s.background(255);
  };
  s.draw = function() {
    s.background(255);
    for(var x = 0; x < movers.length; x += 1) {
      var m = movers[x];
      m.update();
      m.display();
    }
  };
};
