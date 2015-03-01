var p5 = require("p5");
var $ = require("jQuery");

var sketch = require("./sketches/swarm");

$(function() {
  new p5(sketch);
});
