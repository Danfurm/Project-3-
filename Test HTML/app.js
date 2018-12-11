
// Step 1:
// Import data from the donuts.csv file
// =================================
d3.csv("recession.csv", function(error, data) {
  if (error) throw error;
  

var values = data.map(data => data.Recession_Indicator)


var parseTime = d3.timeParse("%Y-%m-%d");

  // Format the data
  data.forEach(function(data) {
    data.date = parseTime(data.Date);
       
    data.value = data.Recession_Indicator;
  });
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

// create svg container
var svg = d3.select("#svg-area").append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// shift everything over by the margins
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);
 
   
   var maxDate = d3.max(data, function(data){ return data.Date; });
   var minDate = d3.min(data, function(data){ return data.Date; });
   var maxprice = d3.max(data, function(data){ return data.value; });

   var y = d3.scaleLinear()
     .domain([0, maxprice])
     .range([chartHeight, 0]);

  var x = d3.scaleTime().domain([minDate, maxDate]).range([0, chartWidth]);
  var yAxis = d3.axisLeft(y);
  var xAxis = d3.axisBottom(x);

  var svg = d3.select('body').append('svg')
              .attr('height', '100%')
              .attr('width', '100%');
  var chartGroup = svg.append('g')
                      .attr('transform', 'translate(50,50)');

  var line = d3.line()
                .x(function(data){ return x(data.date);})
                .y(function(data){ return y(data.value);});
    

  var help = chartGroup.append('path')
  help.attr('d',line(data));
  chartGroup.append('g').attr('class', 'x axis').attr('transform', 'translate(0, '+chartHeight+')').call(xAxis);        
  chartGroup.append('g').attr('class', 'y axis').call(yAxis);        
 });
  