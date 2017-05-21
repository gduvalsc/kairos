class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASYS",
            "icon": "bar-chart",
            "title": "System statistics",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "CPU used (seconds)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORASYSCPU",
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
                                    "query": "DBORANUMCPUS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "Run queue / Load",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "blue" }, "text": { "fill": "blue" } },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASYSRUNQ",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORASYSLOAD",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "IO wait time",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "darkgreen" }, "text": { "fill": "darkgreen" } },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASYSIOWAIT",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
