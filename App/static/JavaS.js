d3.csv("new.csv", function(Data, error) {
  if (error) return console.warn(error);

  console.log(Data);

});
