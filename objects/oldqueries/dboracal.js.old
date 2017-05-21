/*jslint indent: 4, maxerr: 100, vars: true, regexp: true, sloppy: true, node: true, nomen: true, es5: true, evil: true */
var object = {
    type: "query",
    id: "DBORACAL",
    collection: "DBORASTA",
    aggregator: [
        {
            $match: {
                statistic: {
                    $in: [
                        'user calls',
                        'recursive calls'
                    ]
                }
            }
        },
        {
            $project: {
                timestamp: true,
                statistic: true,
                value: true,
                _id: false
            }
        },
        {
            $sort : {
                timestamp: 1
            }
        }
    ]
};
