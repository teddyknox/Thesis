module.exports = function(s) {
  var Agent = function(options) {
    this.options = options;
    this.p = s.createVector(s.random(s.width), s.random(s.height));
    this.pOld = s.createVector(this.p.x, this.p.y);
    this.noiseZVelocity = 0.01;
    this.stepSize = s.random(1,5);
    this.noiseZ;
    this.angle;
    // init noiseZ
    this.setNoiseZRange(0.4);
  };
  Agent.prototype.update1 = function() {
    this.angle = s.noise(
                this.p.x / this.options.noiseScale,
                this.p.y / this.options.noiseScale,
                this.noiseZ) * this.options.noiseStrength;

    this.p.x += s.cos(this.angle) * this.stepSize;
    this.p.y += s.sin(this.angle) * this.stepSize;

    // offscreen wrap
    if (this.p.x <= 10) {
      this.p.x = this.pOld.x = s.width+10;
    }
    if (this.p.x > s.width+10) {
      this.p.x = this.pOld.x = -10;
    }
    if (this.p.y <= 10) {
      this.p.y = this.pOld.y = s.height+10;
    }
    if (this.p.y > s.height+10) {
      this.p.y = this.pOld.y = -10;
    }

    s.strokeWeight(this.options.strokeWidth*this.stepSize);
    s.line(this.pOld.x,this.pOld.y, this.p.x,this.p.y);

    this.pOld.set(this.p);
    this.noiseZ += this.noiseZVelocity;
  };

  Agent.prototype.update2 = function(){
    this.angle = s.noise(this.p.x/this.options.noiseScale ,this.p.y/this.options.noiseScale, this.noiseZ) * 24;
    this.angle = (this.angle - s.int(this.angle)) * this.options.noiseStrength;

    this.p.x += s.cos(this.angle) * this.stepSize;
    this.p.y += s.sin(this.angle) * this.stepSize;

    // offscreen wrap
    if (this.p.x <= 10) {
      this.p.x=this.pOld.x = s.width+10;
    }
    if (this.p.x > s.width+10) {
      this.p.x=this.pOld.x=-10;
    }
    if (this.p.y <= 10) {
      this.p.y=this.pOld.y=s.height+10;
    }
    if (this.p.y > s.height+10) {
      this.p.y=this.pOld.y=-10;
    }

    s.strokeWeight(this.options.strokeWidth * this.stepSize);
    s.line(this.pOld.x,this.pOld.y, this.p.x,this.p.y);

    this.pOld.set(this.p);
    this.noiseZ += this.noiseZVelocity;
  };

  Agent.prototype.setNoiseZRange = function(theNoiseZRange) {
    // small values will increase grouping of the agents
    this.noiseZ = s.random(theNoiseZRange);
  };
  return Agent;
};
