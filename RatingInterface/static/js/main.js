$(function() {

  var transform;
  var START_X = 0;
  var START_Y = 0;
  var ticking = false;

  var reqAnimationFrame = (function () {
	    return window[Hammer.prefixed(window, 'requestAnimationFrame')] || function (callback) {
	        window.setTimeout(callback, 1000 / 60);
	    };
	})();

  function nextImage() {
    $.get('image').then(function(url) {
      $('#canvas').attr('src', url);
    });
  }
  function pretty() {
    $.post($('#canvas').attr('src'), {label: 1}, nextImage);
  }
  function ugly() {
    $.post($('#canvas').attr('src'), {label: 0}, nextImage);
  }
  function resetCanvas() {
	    canvas.className = 'animate';
	    transform = {
	        translate: { x: START_X, y: START_Y },
	        scale: 1,
	        angle: 0,
	        rx: 0,
	        ry: 0,
	        rz: 0
	    };
	    requestElementUpdate();
	}
  function requestElementUpdate() {
	    if(!ticking) {
	        reqAnimationFrame(updateElementTransform);
	        ticking = true;
	    }
	}
  function updateElementTransform() {
	    var value = [
	        'translate3d(' + transform.translate.x + 'px, ' + transform.translate.y + 'px, 0)',
	        'scale(' + transform.scale + ', ' + transform.scale + ')',
	        'rotate3d('+ transform.rx +','+ transform.ry +','+ transform.rz +','+  transform.angle + 'deg)'
	    ];

	    value = value.join(" ");
	    canvas.style.webkitTransform = value;
	    canvas.style.mozTransform = value;
	    canvas.style.transform = value;
	    ticking = false;
	}
  function onPan(ev) {
	    canvas.className = '';
	    transform.translate = {
	        x: START_X + ev.deltaX,
	        y: START_Y + ev.deltaY
	    };
	    requestElementUpdate();
	}
  var canvas = $('#canvas')[0];
  nextImage();
  resetCanvas();

  var mc = new Hammer.Manager(canvas);
  mc.add(new Hammer.Pan({ threshold: 0, pointers: 0}));
  mc.add(new Hammer.Swipe({threshold: 0, velocity: .3})).recognizeWith(mc.get('pan'));
  mc.on("panstart panmove", onPan);
  mc.on("swipeleft", ugly);
  mc.on("swiperight", pretty);
  mc.on("hammer.input", function(ev) {
    if(ev.isFinal) {
        resetCanvas();
    }
  });

  $('#pretty').click(pretty);
  $('#ugly').click(ugly);
  $('body').keydown(function(e) {
    if (e.keyCode == 80) {
      pretty();
    } else if (e.keyCode == 85) {
      ugly();
    }
  });
});
