// Extracting series data from JSON object
var seriesData = [];
Object.keys(json_data).forEach(function(key) {
    var data = Object.values(json_data[key]).map(function(value) {
        return parseFloat(value.toFixed(4));
    });
    seriesData.push({
        name: key,
        data: data
    });
});

var options = {
    series: seriesData,
    chart: {
        type: 'bar',
        height: 350,
    },
    plotOptions: {
        bar: {
            horizontal: false,
        }
    },
    xaxis: {
        categories: Object.keys(json_data["lr"]), // Assuming all datasets have same categories
    },
    yaxis: {
        max: 1.5, // Set your desired maximum value here
        labels: {
            formatter: function(value) {
                return value.toFixed(2);
            }
        }
    },
    legend: {
        position: 'top',
        horizontalAlign: 'right',
        offsetY: -20
    },
    fill: {
        opacity: 1
    }
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();