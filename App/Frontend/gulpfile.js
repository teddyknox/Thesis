"use strict";

var browserify = require('browserify');
var gulp = require('gulp');
var transform = require('vinyl-transform');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');
var browserSync = require('browser-sync');
var reload = browserSync.reload;

// var getBundleName = function () {
//   var version = require('./package.json').version;
//   var name = require('./package.json').name;
//   return version + '.' + name + '.' + 'min';
// };

gulp.task('serve', function() {
    browserSync({
      server: "./dist"
    });
    gulp.watch('./src/css/**', ['css']);
    gulp.watch('./src/js/**', ['js', reload]);
    gulp.watch('./src/index.html', ['html', reload]);
    gulp.watch('./src/img/**', ['img', reload]);
});

gulp.task('js', function () {
  // transform regular node stream to gulp (buffered vinyl) stream
  var browserified = transform(function(filename) {
    var b = browserify(filename);
    return b.bundle();
  });

  return gulp.src('./src/js/index.js')
    .pipe(browserified)
    // .pipe(sourcemaps.init({loadMaps: true}))
        // Add transformation tasks to the pipeline here.
        // .pipe(uglify())
    // .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest('./dist'));
});

gulp.task('html', function() {
  gulp.src('./src/index.html').pipe(gulp.dest('./dist'));
});

gulp.task('img', function() {
  gulp.src('./src/img/**').pipe(gulp.dest('./dist/img'));
});

gulp.task('css', function() {
  gulp.src('./src/css/**')
    .pipe(gulp.dest('./dist'))
    .pipe(reload({stream: true}));
});

gulp.task('default', ['html', 'css', 'js', 'img', 'serve']);
