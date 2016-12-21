/*jslint indent: 4, maxerr: 100, vars: true, regexp: true, sloppy: true, node: true, nomen: true, es5: true, evil: true */
var object = {
    type: "chart",
    id: "TESTPIE",
    icon: "bar-chart",
    title: "Test PIE",
    subtitle: "tbd",
    reftime: "DBORAREFTIME",
    yaxis: [
        {
            position: "left",
            renderers: [
                {
                    type: "P",
                    datasets: [
                        {
                            query: "DBORAWAITEVENTS",
                            timestamp: "timestamp",
                            label: "eclass",
                            value: "time"
                        },
                        {
                            query: "DBORADBCPU",
                            timestamp: "timestamp",
                            label: "statistic",
                            value: "time"
                        }
                    ]
                },
            ]
        },
    ]
};
