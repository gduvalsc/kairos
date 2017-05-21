class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAHITK",
            "icon": "bar-chart",
            "title": " Cache activity - Keep pool - Hit ratio",
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
                                    "query": "DBORAHITKG",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITKR",
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
                                    "query": "DBORAHITKH",
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
                                    "query": "DBORAHITKW",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITKF",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITKB",
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
