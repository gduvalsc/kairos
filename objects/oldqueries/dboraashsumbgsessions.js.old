/*jslint indent: 4, maxerr: 100, vars: true, regexp: true, sloppy: true, node: true, nomen: true, es5: true, evil: true */
var object = {
    type: "query",
    id: "DBORAASHSUMBGSESSIONS",
    collection: "ORAHAS",
    aggregator: [
        {
            $match: {
                session_type : {
                    $in: [
                        'BACKGROUND'
                    ]
                }
            }
        },
        {
            $group: {
                _id: "$timestamp",
                value: { $sum: "$cadsp_count" }
            }
        },
        {
            $project: {
                timestamp: "$_id",
                label: {$literal : "Background DB Time"},
                value: true,
            }
        },
        {
            $sort : {
                timestamp: 1
            }
        }
    ]
};
