var chart;
$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            defaultSeriesType: 'column'
        },
        title: {
            text: '¿Con quien vive Ud en casa?'
        },
        subtitle: {
            text: 'Personas con las que vive en casa'
        },
        xAxis: {
            categories: [
                'Opciones'
            ]
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Cantidad (unidades)'
            }
        },
        legend: {
            layout: 'horizontal',
            //backgroundColor: Highcharts.theme.legendBackgroundColor || '#FFFFFF',
            align: 'left',
            verticalAlign: 'bottom',
            floating: true,
            shadow: true
        },
        tooltip: {
            formatter: function() {
                return ''+
                    this.series.name +': '+ this.y +'';
            }
        },
        plotOptions: {
            column: {
                groupPadding: 0,
                pointPadding: 0.9,
                borderWidth: 0
            },
            series: {
                pointWidth: 30,
                minPointLength : 1
            }
        },
        series: [{% for key, value in tabla.items %}
            {
                name: 'loquesea',
                data: [{{value.0.1}}]
            },
            {% endfor %}]
    });
});


