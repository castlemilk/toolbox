// $(document).ready(function(){

    // $(function () {
    //     // $( "#tabs" ).tabs({
    //     //     activate : function (event,ui) {
    //     //     selectedTabTitle = ui.newTab[0].innerText;
    //     //     alert(selectedTabTitle);
    //     //     }
    //     // });
    //     $('#historical').click('tabsselect', function (event, ui) {
    //             alert($("#historical").tabs('option', 'active');
    //       });
    // });
// });
// ---------------------------------------------------------------------------
// $(function () {
//   var selectedTabTitle = null
//   $(".parent-tabs").tabs();
//   $(".sub-tabs").tabs();
//   $(".sub-tabs").tabs({
//         select: function(event, ui) {
//           selectedTabTitle = $(ui.newTab).text();
//           console.log(selectedTabTitle)
//         }
//   });
// });
// ---------------------------------------------------------------------------

//   var selectedTabTitle = null
//    $("#historical").tabs({
//       activate : function (event,ui) {
//           selectedTabTitle = ui.newTab[0].innerText;
//           alert(selectedTabTitle);
//       }
//   });
// });
// -------------------------- get tab number--------------------------------------------
// $(function () {
//   $("#historical").tabs();
//   $('#historical').click('tabsselect', function (event, ui) {
//         alert($("#historical").tabs('option', 'active'));
//   });
// });
// --------------------------------------------------------------------------
var graph_format1 = {
            chart: {
                zoomType: 'x'
            },
            title: {
                text: ' '
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                        'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
            },
            xAxis: {
                type: 'datetime',
                tickInterval: 30 * 24 * 3600 * 1000,
                min: Date.UTC(1998, 3, 1),
                startOnTick: true,
                labels: {
                    rotation: 45,
                    step: 12,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Arial,sans-serif'
                    }
                },
                dateTimeLabelFormats: { // don't display the dummy year
                    month: '%y',
                    year: '%Y'
                }
            },
            yAxis: {
                title: {
                    text: 'Fuel Price'
                }
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 1
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    // threshold: null,
                    // turboThreshold: 20000,
                },
                series:{
                      pointRange:30 * 24 * 3600 * 1000
                    },
            },

            series: [{
                type: 'area',
                name: '',
                data: [0],
                pointStart: Date.UTC(1998, 3, 1),
                pointInterval: 30 * 24 * 3600 * 1000,
                tooltip: {
                  valueSuffix: '¢/litre',
                        }
            },
            {
                type: 'area',
                name: '',
                data: [0],
                pointStart: Date.UTC(1998, 3, 1),
                pointInterval: 30 * 24 * 3600 * 1000,
                tooltip: {
                valueSuffix: '$/b',
            }
            }
          ]}


$(function () {
  $(".parent-tabs").tabs();
  $(".sub-tabs").tabs();
  $(".sub-tabs").click('tabsselect', function (event, ui) {
    var selected = $(".sub-tabs").tabs('option', 'active');
    console.log(selected)
    var fuel_data = document.getElementById("fuel-graph-data").value;
    var brent_data = document.getElementById("brent-graph-data").value;
    var new_data = {};
    //remove this when you can
    fuel_data = eval(fuel_data)
    brent_data = eval(brent_data)
    var cleaned_data = {}
    for (variable=0; variable<fuel_data.length;variable++) {
      var cleaned_data_row = [];
      for (item=0;item<fuel_data[variable][1].length; item++) {
        if (fuel_data[variable][1][item]=='..' || fuel_data[variable][1][item]=='') {
          cleaned_data_row.push(null)
        }
        else {
          cleaned_data_row.push(fuel_data[variable][1][item])
        }
      }
      cleaned_data[fuel_data[variable][0]] = cleaned_data_row
    }
    var cleaned_data_row_brent = [];
    for (item=0;item<brent_data.length;item++) {
      cleaned_data_row_brent.push(brent_data[item][1])
    }
    var selectedVariable = $($(".sub-tabs li")[selected]).text();
    var selectedVariableData = cleaned_data[selectedVariable]
    console.log(selectedVariableData)

    chart_type = graph_format1
    console.log(chart_type.chart)
    console.log(chart_type.xAxis)
    chart_type.title['text'] = "Fuel Price "+selectedVariable
    chart_type.series[0]['data'] = selectedVariableData
    chart_type.series[0]['name'] = selectedVariable
    chart_type.series[1]['data'] = cleaned_data_row_brent
    chart_type.series[1]['name'] = "brent"

    console.log(chart_type.series[0])
    console.log(brent_data)
    console.log(cleaned_data_row_brent)

    $("#graph1").highcharts(chart_type);

    });
});


// ---------------------------------------------------------------------------
// $(function () {
//   $("#parent-tabs").tabs();
//   $('#parent-tabs').click('tabsselect', function (event, ui) {
//   var selected = $("#parent-tabs").tabs('option', 'active');
//   console.log(selected)
//   });
// });
