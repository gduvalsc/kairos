class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONMEMUSE",
            "icon": "bar-chart",
            "title": "Memory use",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Use (%)",
                    "scaling": "linear",
                    "maxvalue": 110,
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONMEMUSE",
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
