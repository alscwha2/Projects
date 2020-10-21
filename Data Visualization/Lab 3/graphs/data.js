  var anx = [4, 4, 18, 13, 8, 5, 11, 0, 6, 0, 4, 0, 21, 3, 1, 21, 6, 3, 9, 6, 4, 15, 4, 4, 4, 18, 21, 6, 14, 3, 7, 7, 7, 1, 16, 6, 0, 5, 10, 4, 9, 6, 4, 12, 4, 0, 2, 10, 13, 6, 6, 0, 3, 14, 4, 0, 7, 5, 4, 5, 6, 4, 2, 9, 7, 6, 20, 12, 7, 16, 7, 8, 5, 7, 9, 7, 5, 13, 6, 7, 10, 3, 5, 4, 5, 2, 16, 7, 17, 2, 4, 8, 2, 2, 11, 20, 6, 2, 12, 5, 6, 3, 5, 15, 14, 7, 4, 12, 6, 19, 9, 6, 10, 8, 1, 1, 5, 21, 18, 9, 0, 3, 14, 5, 12, 3, 4, 6, 4, 12, 0, 2, 5, 1, 7, 3, 5, 15, 3, 16, 7, 15, 6, 2, 5, 15, 15, 9, 3, 7, 7, 5, 2, 2, 9, 5, 3, 5, 17, 0, 7, 6, 6, 5, 9, 15, 5, 3, 7, 14, 9, 10, 4, 2, 9, 3, 17, 3, 4, 16, 2, 2, 11, 4, 3, 14, 8, 4, 9, 3, 18, 9, 5, 5, 3, 21, 6, 4, 4, 6, 13, 6, 12, 6, 15, 7, 11, 16, 6, 1, 4, 1, 18, 11, 18, 19, 6, 8, 11, 3, 15, 6, 5, 13, 0, 14, 8, 18, 5, 19, 10, 2, 14, 6, 7, 1, 14, 0, 10, 7, 0, 0, 7, 0, 0, 10, 21, 0, 1, 5, 0, 7, 21, 0, 0, 0, 0, 11, 0, 0, 0, 0, 2, 0, 0, 7, 14, 0, 7, 0, 0, 0, 0, 7, 21, 0, 3, 7, 0, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 21, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 14, 14, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 12, 7, 2, 3, 7, 2, 0, 11, 3, 0, 1, 0, 0, 0, 1, 0, 0, 12, 3, 0, 0, 3, 2, 0, 0, 0, 6, 0, 3, 2, 0, 14, 0, 0, 2, 15, 0, 0, 16, 5, 0, 0, 0, 3, 10, 6, 18, 6, 5, 12, 1, 10, 1, 0, 1, 0, 3, 3, 0, 14, 0, 5, 3, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 18, 0, 0, 0, 0];

  var dep = [3, 3, 17, 12, 9, 6, 6, 5, 10, 1, 7, 0, 19, 4, 2, 27, 2, 5, 2, 8, 3, 13, 7, 2, 5, 19, 18, 8, 18, 2, 3, 8, 1, 2, 17, 1, 1, 7, 5, 2, 5, 1, 9, 19, 2, 3, 5, 8, 16, 6, 6, 0, 2, 23, 1, 5, 11, 1, 6, 13, 5, 2, 4, 12, 5, 0, 21, 12, 4, 22, 6, 6, 5, 10, 5, 2, 8, 8, 15, 17, 9, 2, 4, 2, 5, 3, 8, 4, 24, 1, 0, 8, 3, 2, 17, 18, 9, 0, 6, 2, 8, 9, 2, 14, 7, 1, 5, 10, 5, 9, 4, 7, 13, 5, 0, 5, 3, 18, 24, 2, 0, 5, 23, 2, 9, 2, 5, 2, 4, 9, 1, 21, 4, 8, 2, 1, 3, 16, 1, 14, 17, 10, 3, 4, 7, 15, 8, 12, 1, 4, 5, 3, 1, 6, 6, 10, 2, 8, 8, 14, 8, 7, 3, 1, 15, 14, 9, 1, 9, 20, 5, 8, 1, 7, 11, 7, 17, 6, 3, 24, 2, 2, 13, 6, 8, 6, 1, 4, 8, 4, 11, 12, 5, 14, 5, 23, 4, 6, 2, 3, 16, 8, 9, 3, 10, 3, 16, 13, 5, 0, 2, 6, 16, 16, 20, 26, 8, 15, 4, 7, 12, 6, 7, 4, 1, 12, 9, 7, 5, 14, 3, 2, 15, 6, 4, 2, 8, 0, 0, 9, 0, 0, 0, 0, 0, 6, 16, 0, 1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 8, 0, 0, 24, 0, 0, 0, 0, 24, 8, 0, 1, 24, 0, 16, 16, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 16, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 8, 0, 0, 0, 0, 16, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 16, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 8, 0, 0, 5, 2, 0, 14, 1, 0, 3, 0, 2, 2, 1, 0, 0, 2, 4, 0, 0, 2, 7, 1, 0, 0, 0, 0, 0, 1, 0, 13, 0, 1, 0, 18, 3, 7, 8, 4, 0, 0, 2, 3, 22, 2, 27, 1, 5, 7, 0, 2, 1, 0, 2, 0, 5, 5, 2, 12, 0, 3, 2, 0, 14, 0, 2, 0, 0, 2, 0, 1, 0, 0, 2, 0, 2, 0, 0, 0, 19, 0, 1, 3, 0];

  var adolDep = [4, 1, 6, 5, 3, 1, 1, 3, 7, 10, 6, 0, 1, 4, 9, 9, 7, 3, 0, 12, 7, 9, 8, 1, 3, 7, 4, 6, 10, 0, 14, 6, 4, 2, 7, 0, 5, 0, 5, 1, 12, 8, 2, 1, 0, 0, 4, 15, 5, 22, 6, 0, 0, 0, 16, 4, 5, 4, 2, 18, 9, 11, 5, 8, 3, 1, 10, 5, 7, 2, 4, 6, 5, 4, 1, 0, 0, 5, 3, 3, 6, 4, 10, 11, 6, 2, 12, 6, 5, 7, 20, 7, 6, 6, 0, 10, 0, 5, 3, 2, 0, 0, 1, 4, 2, 1, 1, 15, 3, 10, 7, 11, 4, 3, 3, 2, 3, 6, 1, 0, 1, 4, 3, 2, 3, 3, 1, 10, 2, 12, 6, 3, 2, 5, 10, 12, 17, 4, 10, 23, 6, 0, 1];

  var scared = [1, 2, 7, 0, 1, 1, 0, 1, 2, 4, 1, 1, 0, 2, 1, 3, 4, 2, 1, 2, 2, 1, 5, 4, 3, 0, 1, 1, 8, 1, 4, 0, 1, 3, 2, 3, 2, 4, 4, 1, 1, 6, 2, 1, 0, 0, 1, 2, 3, 4, 0, 4, 0, 1, 7, 0, 1, 0, 1, 1, 4, 1, 1, 1, 3, 0, 2, 1, 4, 1, 1, 2, 2, 7, 3, 0, 0, 5, 1, 1, 2, 0, 0, 2, 1, 3, 1, 6, 1, 2, 5, 2, 1, 6, 0, 2, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 3, 2, 1, 4, 1, 1, 2, 1, 3, 3, 4, 0, 0, 2, 2, 2, 0, 2, 3, 0, 3, 1, 4, 0, 1, 6, 0, 4, 7, 3, 1, 3, 9, 1, 0, 0];

  var gad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 1, 9, 5, 1, 1, 0, 0, 2, 4, 5, 15, 7, 4, 1, 9, 18, 0, 11, 0, 3, 5, 12, 6, 3, 11, 1, 2, 9, 4, 12, 4, 3, 8, 2, 10, 0, 3, 1, 5, 0, 4, 7, 7, 3, 9, 2, 2, 8, 12, 4, 3, 17, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 2, 3, 4, 10, 3, 4, 3, 5, 3, 5, 1, 0, 2, 5, 4, 3, 5, 3, 0, 4, 0, 19, 4, 1, 0, 3, 2, 4, 14, 3, 6, 21, 7, 0, 0];
  /*
  Takes the two arrays of equal length with the information for two columns.
  Returns a new array of same length which, for each data point, gives the size of the bubble.
  The size of the bubble for each data point is (currently) 10*the number of overlapping points.
  */
  var getSizes = function(ar1, ar2) {
    //make empty 2D array
    var freq = [];
    for (var i = 0; i < Math.max(...ar1) + 1; i++) {
      var arr = [];
      for (var j = 0; j < Math.max(...ar2) + 1; j++) arr.push(0);
      freq.push(arr);
    }
    //fill 2D array
    for (var i = 0; i < ar1.length; i++) {
      freq[ar1[i]][ar2[i]]++;
    }
    //get rid of 0,0 that messes us up.
    freq[0][0] = 0;

    //turn into 1D array
    var linkedfreq = [];
    for (var i = 0; i < ar1.length; i++) {
      linkedfreq.push(freq[ar1[i]][ar2[i]]);
    }
    //get size
    //var max = Math.max(...linkedfreq);
    for (var i = 0; i < linkedfreq.length; i++) {
      //linkedfreq[i] = parseFloat(linkedfreq[i]) / parseFloat(max);
      linkedfreq[i] *= 10;
    }
    return linkedfreq;
  }
  /*
  Takes an array of arrays. The interior arrays are of format [color, minscore - 0.5, maxscore + 0.5]
  These interior arrays should represent the color code in the excel document for these scores.
  Returns an array of shapes to be appended to layout.shapes and should serve as a legend.
  */
  var createShapes = function(source, isxaxis)
  {
    var dest = [];
    for (var i = 0; i < source.length; i++)
    {
      var col = source[i];
      var rec = {};
      rec.fillcolor = col[0];
      rec.line = {"width": 0};
      rec.opacity = 0.5;
      rec.type = "rect";
      rec.yref = "y";
      rec.xref = "x";
      rec.layer = "below";
      if (!isxaxis) {
        rec.y0 = col[1];
        rec.y1 = col[2];
        rec.x0 = -1.5;
        rec.x1 = -0.5;
      }
      if (isxaxis) {
        rec.x0 = col[1];
        rec.x1 = col[2];
        rec.y0 = -1.5;
        rec.y1 = -0.5;
      }
      dest.push(rec);
    }
    return dest;
  }

  /*
  Does it for you automatically.
  */
  var swapAxes = function() {
  	var temp = trace.y;
  	trace.y = trace.x;
  	trace.x = temp;

  	temp = layout.xaxis.title;
  	layout.xaxis.title = layout.yaxis.title;
  	layout.yaxis.title = temp;

  	for (var i = 0; i < layout.shapes.length; i++) {
  	  shape = layout.shapes[i];
  	  temp = shape.y0;
  	  shape.y0 = shape.x0;
  	  shape.x0 = temp;

        temp = shape.y1;
  	  shape.y1 = shape.x1;
  	  shape.x1 = temp;

  	  if (shape.x1 < 0 && shape.x0 < 0) shape.x0 = -1;
  	  if (shape.y1 < 0 && shape.y0 < 0) shape.y0 = -2;
  	}
  }

  /*
  Sets layout.shapes to a NEW array of NEW shape objects. That means that you can save 
    the old values in a local variable and restore them.
  */
  var extendX = function()
  {
  	var max = 0;
  	var min = 100;
  	var shps = layout.shapes;
    for(var i = 0; i < shps.length; i++) {
      var shp = shps[i];
      if (shp.y0 != -1.5 && shp.y1 > max) max = shp.y1;
      if (shp.y0 < min) min = shp.y0;
    }

    var newshps = [];
    for (var i = 0; i < shps.length; i++) {
      var shp = shps[i];
      var newshp = {};
      for (var attr in shp) {
        newshp[attr] = shp[attr];
      }
      if (newshp.y0 == min) {
        newshp.y1 = max
        newshp.opacity = 0.2;
      }
      newshps.push(newshp);
    }
    layout.shapes = newshps;
  }
  var extendY = function()
  {
    var max = 0;
    var min = 100;
    var shps = layout.shapes;
    for(var i = 0; i < shps.length; i++) {
      var shp = shps[i];
      if (shp.x0 != -1.5 && shp.x1 > max) max = shp.x1;
      if (shp.x0 < min) min = shp.x0;
    }

    var newshps = [];
    for (var i = 0; i < shps.length; i++) {
      var shp = shps[i];
      var newshp = {};
      for (var attr in shp) {
        newshp[attr] = shp[attr];
      }
      if (newshp.x0 == min) {
        newshp.x1 = max
        newshp.opacity = 0.2;
      }
      newshps.push(newshp);
    }
    layout.shapes = newshps;
  }

  /*
  For first two graphs in adults.
  */
  var myHighlights = [
    {
      "fillcolor": "ff9999",
      "line": {"width": 0},
      "opacity": 0.5,
      "type": "rect",
      "x0": -0.5,
      "x1": 4.5,
      "xref": "x",
      "y0": 0,
      "y1": 28,
      "yref": "y",
      "layer": "below"
    },
    {
      "fillcolor": "66b266",
      "line": {"width": 0},
      "opacity": 0.5,
      "type": "rect",
      "x0": 4.5,
      "x1": 7.5,
      "xref": "x",
      "y0": 0,
      "y1": 28,
      "yref": "y",
      "layer": "below"
    },
    {
      "fillcolor": "ef8eef",
      "line": {"width": 0},
      "opacity": 0.5,
      "type": "rect",
      "x0": 7.5,
      "x1": 22,
      "xref": "x",
      "y0": 0,
      "y1": 28,
      "yref": "y",
      "layer": "below"
    }];