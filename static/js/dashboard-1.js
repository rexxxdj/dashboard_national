(function($) {
    "use strict";



    // Morris bar chart
    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '2022',
            "Загальний фонд": 4000000,
            "ПДФО 10%": 200000,
            "Субвенція": 700000,
            "Благодійна допомога": 40000
        }, {
            y: '2023',
            "Загальний фонд": 12000000,
            "ПДФО 10%": 2200000,
            "Субвенція": 3700000,
            "Благодійна допомога": 10000000
        }, {
            y: '2024',
            "Загальний фонд": 40000000,
            "ПДФО 10%": 22200000,
            "Субвенція": 30700000,
            "Благодійна допомога": 20000000
        }, {
            y: '2025',
            "Загальний фонд": 20000,
            "ПДФО 10%": 20000,
            "Субвенція": 5000,
            "Благодійна допомога": 100000
        }],
        xkey: 'y',
        ykeys: ['Загальний фонд', 'ПДФО 10%', 'Субвенція', 'Благодійна допомога'],
        labels: ['Загальний фонд', 'ПДФО 10%', 'Субвенція', 'Благодійна допомога'],
        barColors: ['#343957', '#5873FE','#2dc466','#d2a01b'],
        hideHover: 'auto',
        gridLineColor: '#eef0f2',
        resize: true
    });

    $('#info-circle-card').circleProgress({
        value: 0.70,
        size: 100,
        fill: {
            gradient: ["#a389d5"]
        }
    });

    $('.testimonial-widget-one .owl-carousel').owlCarousel({
        singleItem: true,
        loop: true,
        autoplay: false,
        //        rtl: true,
        autoplayTimeout: 2500,
        autoplayHoverPause: true,
        margin: 10,
        nav: false,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });



})(jQuery);

(function($) {
    "use strict";

    var data = [],
        totalPoints = 300;

    function getRandomData() {

        if (data.length > 0)
            data = data.slice(1);

        // Do a random walk

        while (data.length < totalPoints) {

            var prev = data.length > 0 ? data[data.length - 1] : 50,
                y = prev + Math.random() * 10 - 5;

            if (y < 0) {
                y = 0;
            } else if (y > 100) {
                y = 100;
            }

            data.push(y);
        }

        // Zip the generated y values with the x values

        var res = [];
        for (var i = 0; i < data.length; ++i) {
            res.push([i, data[i]])
        }

        return res;
    }

    // Set up the control widget

    var updateInterval = 30;
    $("#updateInterval").val(updateInterval).change(function() {
        var v = $(this).val();
        if (v && !isNaN(+v)) {
            updateInterval = +v;
            if (updateInterval < 1) {
                updateInterval = 1;
            } else if (updateInterval > 3000) {
                updateInterval = 3000;
            }
            $(this).val("" + updateInterval);
        }
    });

    var plot = $.plot("#cpu-load", [getRandomData()], {
        series: {
            shadowSize: 0 // Drawing is faster without shadows
        },
        yaxis: {
            min: 0,
            max: 100
        },
        xaxis: {
            show: false
        },
        colors: ["#007BFF"],
        grid: {
            color: "transparent",
            hoverable: true,
            borderWidth: 0,
            backgroundColor: 'transparent'
        },
        tooltip: true,
        tooltipOpts: {
            content: "Y: %y",
            defaultTheme: false
        }


    });

    function update() {

        plot.setData([getRandomData()]);

        // Since the axes don't change, we don't need to call plot.setupGrid()

        plot.draw();
        setTimeout(update, updateInterval);
    }

    update();


})(jQuery);

const wtl = new PerfectScrollbar('.widget-timeline');