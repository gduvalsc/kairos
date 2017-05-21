class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASUM",
            "icon": "bar-chart",
            "title": "DB CPU & Wait - Gets - Reads - Redo size",
            "subtitle": "",
            "collections": ['DBORAMISC', 'DBORATMS','DBORAWEC','DBORASTA'],
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORASUMWAITEVENTS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORADBCPU",
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
                                    "query": "DBORADBTIME",
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
                                    "query": "DBORALOGREADS",
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
                                    "query": "DBORAPHYREADS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of redo bytes per second",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "blue" }, "text": { "fill": "blue" } },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAREDOBYTES",
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
