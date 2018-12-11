// svg container
var svgHeight = 400;
var svgWidth = 1000;

// margins
var margin = {
  top: 50,
  right: 50,
  bottom: 50,
  left: 50
};

// chart area minus margins
var chartHeight = svgHeight - margin.top - margin.bottom;
var chartWidth = svgWidth - margin.left - margin.right;

var x = d3.time.scaleLinear().range([0, chartWidth]);
var y = d3.scale.linear().range([chartHeight, 0]);

// Step 1:
// Import data from the donuts.csv file
// =================================
d3.csv("recession.csv", function(error, data) {
  if (error) throw error;
  console.log(data)

var values = data.map(data => data.Recession_Indicator)
console.log(values)

var parseTime = d3.timeParse("%Y-%m-%d");

  // Format the data
  data.forEach(function(data) {
    data.date = parseTime(data.Date);
       console.log(data)
    data.value = data.Recession_Indicator;
    
    x.domain(data.map(function(data) { return data.Date; }));
    y.domain([0, d3.max(data, function(data) { return data.value; })]);   
 });
  
 var lineGenerator = d3.line();

console.log("Drawing commands:", lineGenerator(data.values));

var svg = d3.select("#path-2");

svg.append("path")
  .attr("fill", "none")
  .attr("stroke", "blue")
  .attr("stroke-width", 5)
  .attr("d", lineGenerator(data.values));



});