$(document).ready(function() {
    var realtimeChart;
    var dataTable;

    function drawChart(data) {
        if (realtimeChart) {
            realtimeChart.destroy();
        }

        realtimeChart = new Chart($("#realtime-chart"), {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Real-time Financial Data'
                },
                scales: {
                    xAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Time'
                        }
                    }],
                    yAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Value'
                        }
                    }]
                }
            }
        });
    }

    function updateTable(data) {
        if (dataTable) {
            dataTable.destroy();
        }

        dataTable = $('#data-table').DataTable({
            data: data,
            columns: [
                { title: "Time" },
                { title: "Value" }
            ]
        });
    }

    function fetchData() {
        $.ajax({
            url: '/fetch_data',
            method: 'GET',
            success: function(data) {
                drawChart(data);
                updateTable(data);
            },
            error: function(error) {
                console.error("Error fetching data: ", error);
            }
        });
    }

    $("#update-button").click(function() {
        fetchData();
    });

    fetchData();
});