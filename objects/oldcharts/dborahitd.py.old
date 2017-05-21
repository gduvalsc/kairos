class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAHITD",
            "icon": "bar-chart",
            "title": " Cache activity - Default pool - Hit ratio",
            "subtitle": "",
            "yaxis": [
                {
                    "title": "Number of buffer gets / reads per second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORAHITDG",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITDR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        }
                    ]
                },
                {
                    "title": "Hit ratio (%)",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "red" }, "text": { "fill": "red" } },
                    "maxvalue": 101,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHITDH",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        }
                    ]
                },
                {
                    "title": "Waits per second",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHITDW",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITDF",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITDB",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
