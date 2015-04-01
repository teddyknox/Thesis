var _ = require("lodash");

module.exports = function(s) {
  var Triangle = function(color, points) {
    this.color = color || [s.random(255), s.random(255), s.random(255), s.random(255)];
    this.points = points || [Math.round(s.random(s.width)), Math.round(s.random(s.height)),
                             Math.round(s.random(s.width)), Math.round(s.random(s.height)),
                             Math.round(s.random(s.width)), Math.round(s.random(s.height))];
  };
  s.setup = function() {
    s.createCanvas(s.windowWidth, s.windowHeight);
    s.noLoop();
  };
  s.draw = function() {
    s.background(s.random(255), s.random(255), s.random(255));
    s.strokeCap(s.ROUND);
    s.strokeJoin(s.ROUND);
    s.strokeWeight(2);
    var triangles = [];
    _.times(s.int(s.random(10)), function() {
      var tri = new Triangle();
      var color = tri.color;
      triangles.push(tri);
      triangles.concat(_.times(s.int(s.random(10)), function() {
        return new Triangle(color);
      }));
      _(triangles).shuffle().each(function(t) {
        s.fill.apply(s, t.color);
        s.stroke.apply(s, t.color);
        s.triangle.apply(s, t.points);
      }).value();
    });
  };
  s.mouseClicked = function() {
    s.redraw();
  };
};
