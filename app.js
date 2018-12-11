
// Step 1:
// Import data from the donuts.csv file
// =================================
d3.csv("recession.csv", function(error, data) {
  if (error) throw error;
  console.log(data)

// var values = data.map(data => data.Recession_Indicator)
// console.log(values)

// var parseTime = d3.timeParse("%m-%Y");

//   // Format the data
//   data.forEach(function(data) {
//     data.date = parseTime(data.date);
//        console.log(data)  
// });
    



});