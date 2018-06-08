class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONMEMUSE",
            "title": "Memory use",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Use (%)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONMEMUSE$$1",
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