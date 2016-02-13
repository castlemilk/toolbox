

$(document).ready(function(){
  var P_t = [];
  var T_t = [];
  var c = 0;
    // $("#MortgageForm").submit(function(){
    //   // P_t = [];
    //   // T_t = [];
    //   // calculateResults();
    //   // chart_type = chartOptions_spline;
    //   // chart_type.series[0]['data'] = P_t
    //   // chart_type.series[1]['data'] = T_t
    //   // $('#MortgageGraph').highcharts(chart_type);
    //   // generateReport();
    //   return true
    //   // $('#MortgageForm').data("Principle", P_t);
    //   // $('#MortgageForm').data("Total Payed",T_t);
    //   // chart.series[0].setData(data,true);
    // });
    var chartOptions_spline = {
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Loan Repayment over time'
        },

        xAxis: {
            type: 'years',
            allowDecimals: false,
            labels: {
                formatter: function () {
                    return this.value; // clean, unformatted number for year
                }
            }
        },
        yAxis: {
            title: {
                text: 'Amount remaining ($)'
            },
            minorGridLineWidth: 0,
            gridLineWidth: 0,
            alternateGridColor: null,

        },
        tooltip: {
            valueSuffix: ' AUD ($)'
        },
        plotOptions: {
            spline: {
                lineWidth: 4,
                states: {
                    hover: {
                        lineWidth: 5
                    }
                },
                marker: {
                    enabled: false
                },
                pointInterval: 1, // one hour
                pointStart: 0
            }
        },
        series: [{
            name: 'Principle Remaining',
            data: [0]

        }, {
            name: 'Principle + Interest Remaining',
            data: [0]
        }],
        navigation: {
            menuItemStyle: {
                fontSize: '10px'
            }
        }
    }
    chart_type = chartOptions_spline;
    console.log(chart_type)


    calculateResults();
    console.log(P_t)
    console.log(T_t)
    chart_type.series[0]['data'] = P_t
    chart_type.series[1]['data'] = T_t
    $('#MortgageGraph').highcharts(chart_type);
    generateReport();

    function calculateResults(){
      var $inputs = $("#MortgageForm :input");
      var values = {};
      $inputs.each(function() {
        values[this.name] = $(this).val();
      });
      loan_value = values['loan_value']
      loan_value =loan_value.replace(/,/g, '')
      loan_value = parseInt(loan_value)

      var N_total = values['loan_period']*12;// period [months]
      var r = values['interest_rate']/100/12; //interest rate [interest per month]
      var P_0 = parseInt(values['loan_value'].replace(/,/g, ''));//principle loan amount


      c = monthlyRepayment(r,N_total,P_0)
      var plot_start = 0;
      var plot_finish = values['loan_period'];
      var time_series = [];
      for (var i = plot_start; i<=plot_finish; i++){
          time_series.push(i);
      }
      for (var i=0;i<=time_series.length-1; i++){
        var N_t = i*12;
        var P_n = principleRemaining(c,r,N_t,P_0);
        P_t.push(P_n);
      }
      var I = c*N_total-P_0;
      for (var i=0; i<=time_series.length-1; i++){
        var N_t = i*12;
        var T_n = totalRemaining(I,N_total,N_t,P_0);
        T_t.push(T_n);
      }

        function monthlyRepayment(r,N,P){
          return (r/(1-Math.pow((1+r),-1*N)))*P // monthly repayment
        }
        function principleRemaining(c,r,N,P_0){
          S = (Math.pow(1+r,N)-1)/r;
          return Math.round(P_0*Math.pow(1+r,N) - c*S)
        }
        function totalRemaining(I,N_total,x,P_0){
          var m = (P_0+I)/N_total;
          var b = P_0+I;
          var y = Math.round(-1*m*x+b);
          return y
        }
    }
    function generateReport() {
      console.log("generating report")
      per_month= Math.round(c)
      per_fortnight = Math.round(per_month/2)
      per_week = Math.round(per_month/4)
      total_interest = Math.round(T_t[0]-P_t[0])
      var separator = $("</div>",{"text":"<span></span>","class":"fancy"});
      // });
      $('p.fancy').replaceWith('<p class="fancy" ><span></span></p>');
      console.log($('.fancy'))
      console.log(separator)
      $('.report').fadeIn(1500);
      // if ($('.repayment_monthly').length){
      $('.monthly').children('.monthly_text').text('Monthly Repayment: ');
      $('.monthly').children('.monthly_value').text("$"+per_month);
      // $('.monthly').children('p').append('<span></span>');
      $('.fortnightly').children('.fortnightly_text').text('Fortnightly Repayment: ');
      $('.fortnightly').children('.fortnightly_value').text("$"+per_fortnight);
      // $('.fortnightly').text("Fornightly Repayment: "+"$"+per_fortnight);
      $('.weekly').children('.weekly_text').text('Weekly Repayment: ');
      $('.weekly').children('.weekly_value').text("$"+per_week);
      // $('.weekly').text("Weekly Repayment: "+"$"+per_week);
      // $('.total_interest').text("Total Interest payed: "+"$"+total_interest);
      $('.total_interest').children('.total_interest_text').text('Total Interest Payed: ');
      $('.total_interest').children('.total_interest_value').text("$"+total_interest);
      //
      // }
      // else {
        // $('monreport').append(monthly_repayment);
      // }

    };

    var chartOptions_area = {
      chart: {
          type: 'area'
      },
      title: {
          text: 'Loan Repayment'
      },
      // subtitle: {
      //     text: ''
      // },
      xAxis: {
          allowDecimals: false,
          labels: {
              formatter: function () {
                  return this.value; // clean, unformatted number for year
              }
          }
      },
      yAxis: {
          title: {
              text: 'Amount Remaining ($)'
          },
          labels: {
              formatter: function () {
                  return this.value / 1000 + 'k';
              }
          }
      },
      tooltip: {
          pointFormat: '{series.name} Remaining &lt;b&gt;{point.y:,.0f}&lt;/b&gt;&lt;br/&gt;After {point.x} years '
      },
      plotOptions: {
          area: {
              pointStart: 0,
              marker: {
                  enabled: false,
                  symbol: 'circle',
                  radius: 2,
                  states: {
                      hover: {
                          enabled: true
                      }
                  }
              }
          }
      },
      series: [{
          name: 'Principle',
          data: [0]
      }, {
          name: 'Principle + Interest',
          data: [0]
      }]
    }
  
});

  // console.log("Inside submit function")
  // console.log("global var P_t")
  // console.log(T_t)
  // console.log("function data store:")
  // console.log($('#MortgageForm').data("Principle"))
  // });
  // console.log("Outside submit function:")
  // console.log(P_t)
  // console.log($('#MortgageForm').data("Total Payed"))
  // });
  // console.log("Outside main document :")
  // console.log(P_t)
  //
  // console.log("Tests: ")
  // console.log(window.time_series)
