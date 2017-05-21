class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONSYS",
            "icon": "bar-chart",
            "title": "Statistics",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Value",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONSYS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
