class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAHITR",
            "icon": "bar-chart",
            "title": " Cache activity - Recycle pool - Hit ratio",
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
                                    "query": "DBORAHITRG",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITRR",
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
                                    "query": "DBORAHITRH",
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
                                    "query": "DBORAHITRW",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITRF",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHITRB",
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
