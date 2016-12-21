class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONMEMOV",
            "icon": "bar-chart",
            "title": "Memory overview",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Memory size (MB)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONMEMOV",
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
