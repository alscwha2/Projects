function addTooltip(popLookup) {
	console.log(window.popData);
var tip = d3.tip()
  .attr('class', 'd3-tip')
  .style("background-color", "#e8eaed")
  .style("font-family", "sans-serif")
  .offset([40, 100])
  .html(function(d){return d.properties.county_nam + ": " + popLookup.get(d.properties.county_nam);});

var vis = d3.select("#map svg")
  // REQUIRED:  Call the tooltip on the context of the visualization
  .call(tip);

vis.on('mouseout', tip.hide);

var counties = vis.selectAll(".county");
  // Show and hide the tooltip
  counties.on('mouseover', tip.show);
  counties.on('mouseout', tip.hide);
}

function addBrushing() {
	var counties = d3.select("#map svg").selectAll(".county")
	.on('mouseenter', function(d) {
		d3.select(this).classed("current", true);
		d3.select("#bar svg").selectAll(".bar rect")
			.classed("current", function(e) {
				if (e.County == d.properties.county_nam) {
					return true;
				}
				return false;
			})
	})
	.on('mouseout', function() {
		d3.select(this).classed("current", false);
		d3.select("#bar svg").selectAll(".bar rect")
			.classed("current", false);
	});

	var bars = d3.selectAll(".bar rect")
	.on('mouseenter', function(e) {
		d3.select(this).classed("current", true);
		d3.selectAll(".county")
			.classed("current", function(d) {
				if (e.County == d.properties.county_nam) {
					return true;
				}
				return false;
			})
	})
	.on('mouseout', function() {
		d3.select(this).classed("current", false);
		d3.selectAll(".county")
			.classed("current", false);
	});
}

function addDistortion() {

}

function addHistogram(popData) {

}

function addToVisualization() {
    addTooltip(window.popLookup);
    addDistortion();
    addBrushing();
    // for extra credit
    addHistogram(window.popData);
}

// do not remove the getData call!
getData(addToVisualization);