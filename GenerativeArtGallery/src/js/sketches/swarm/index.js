var _ = require("lodash");

module.exports = function(s) {
  var Agent = require("./agent")(s);
  // ------ agents ------
  var agents;
  var agentsCount = 1000;
  var overlayAlpha = 1;
  var agentsAlpha = 90;
  var drawMode = 1;

  // ------ ControlP5 ------
  // ControlP5 controlP5;
  // var showGUI = false;
  // var sliders;

  s.setup = function(){
    s.createCanvas(s.windowWidth, s.windowHeight);
    s.smooth();

    agents = _.times(agentsCount, function() {
      return new Agent({
        noiseScale: 100,
        noiseStrength: 10,
        noiseZRange: 0.4,
        strokeWidth: 0.3
      });
    });

    // setupGUI();
  };

  s.draw = function(){
    var i;
    s.fill(255, overlayAlpha);
    s.noStroke();
    s.rect(0,0,s.width,s.height);

    s.stroke(0, agentsAlpha);
    //draw agents
    if (drawMode === 1) {
      for(i = 0; i < agentsCount; i++) {
        agents[i].update1();
      }
    } else {
      for(i = 0; i < agentsCount; i++) {
        agents[i].update2();
      }
    }

    // drawGUI();
  };

  // s.keyReleased = function(){
  //   if (key === 'm' || key === 'M') {
  //     // showGUI = controlP5.group("menu").isOpen();
  //     // showGUI = !showGUI;
  //   }
  //   if (showGUI) controlP5.group("menu").open();
  //   else controlP5.group("menu").close();
  //
  //   if (key == '1') drawMode = 1;
  //   if (key == '2') drawMode = 2;
  //   if (key=='s' || key=='S') saveFrame(timestamp()+".png");
  //   if (key == DELETE || key == BACKSPACE) background(255);
  // }

  // var timestamp() {
  //   return String.format("%1$ty%1$tm%1$td_%1$tH%1$tM%1$tS", Calendar.getInstance());
  // }

};
