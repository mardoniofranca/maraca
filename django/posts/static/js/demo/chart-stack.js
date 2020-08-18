window.chartColors = {
  red: 'rgb(255, 99, 132)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(231,233,237)'
};
var barChartData = {
  labels: ['Perfil 1', 'Perfil 2', 'Perfil 3'],
  datasets: [{
    label: 'L1',
    backgroundColor: window.chartColors.red,
    stack: 'Stack 0',
    data: [10]
  }, {
    label: 'L2',
    backgroundColor: window.chartColors.orange,
    stack: 'Stack 0',
    data: [20]
  },
  {
    label: 'L3',
    backgroundColor: window.chartColors.yellow,
    stack: 'Stack 1',
    data: [0,10]
  },
  {
    label: 'L4',
    backgroundColor: window.chartColors.green,
    stack: 'Stack 1',
    data: [0,20]
  }, {
    label: 'L5',
    backgroundColor: window.chartColors.blue,
    stack: 'Stack 1',
    data: [0,30]
  }, {
    label: 'L6',
    backgroundColor: window.chartColors.grey,
    stack: 'Stack 2',
    data: [0,0,10]
  },
  {
    label: 'L7',
    backgroundColor: window.chartColors.purple,
    stack: 'Stack 2',
    data: [0,0,20]
  }]
};
window.onload = function() {
  var ctx = document.getElementById('canvas').getContext('2d');
  window.myBar = new Chart(ctx, {
    type: 'bar',
    data: barChartData,
    options: {
      tooltips: {
        mode: 'index',
        intersect: false
      },
      responsive: true,
      scales: {
        xAxes: [{
          stacked: true,
        }],
        yAxes: [{
          stacked: true
        }]
      }
    }
  });
};
