var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: ["Unit A", "Unit B", "Unit C", "Unit D"],
        datasets: [{
            label: "Years Spent in Each Unit",
            data: [5, 3, 7, 11]
        }]
    }
});
console.log(123)


// Get the canvas element
var ctx = document.getElementById('myChart').getContext('2d');

// Define the data for the chart
var data = {
  labels: ['Unit A', 'Unit B', 'Unit C', 'Unit D'],
  datasets: [{
    label: 'Number of Years',
    data: [5, 3, 8, 11],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(255, 206, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)'
    ],
    borderColor: [
      'rgba(255, 99, 132, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(255, 206, 86, 1)',
      'rgba(75, 192, 192, 1)'
    ],
    borderWidth: 1
  }]
};

// Define the options for the chart
var options = {
  scales: {
    yAxes: [{
      ticks: {
        beginAtZero: true
      }
    }]
  }
};

// Create the chart
var myChart = new Chart(ctx, {
  type: 'bar',
  data: data,
  options: options
});


