class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACSUM",
            "icon": "bar-chart",
            "title": "RAC summary - CPU - Wait events - Gets - Reads - Redo",
            "subtitle": "",
            "collections": ['DBORARACMISC', 'DBORARACTM','DBORARACTTFE','DBORARACSTA'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACSUMWAITEVENTS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORARACDBCPU",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACDBTIME",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "# of logical reads per second",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "darkgreen" }, "text": { "fill": "darkgreen" }},
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACLOGREADS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of physical reads per second",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "red" }, "text": { "fill": "red" } },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACPHYREADS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of redo bytes second",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "blue" }, "text": { "fill": "blue" } },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACREDOBYTES",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"

                                }
                            ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
