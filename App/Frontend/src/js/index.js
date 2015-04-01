var _ = require("lodash");
var $ = require("jQuery");
var p5 = require("p5");
var sketches = require("./sketches");

var path = window.location.pathname.substring(1);
var sketch = sketches[path];
if (sketch) {
  new p5(sketch);
} else {
  var html = '<div class="container"><h1>Processing Sketches for Thesis</h1><ul>';
  _.each(_.keys(sketches), function(name) {
    html += '<li><a href="/' + name + '">' + name + '</a></li>';
  });
  html += '</ul><div>';
  $("body").html(html);
}
