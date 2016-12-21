class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAFILR",
            "icon": "bar-chart",
            "title": "Database file reads",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of I/O reads per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAFILR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                    ]
                },
                {
                    "title": "# of blocks reads per second",
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
                                },
                            ]
                        },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
