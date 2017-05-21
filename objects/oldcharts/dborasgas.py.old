class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASGAS",
            "icon": "bar-chart",
            "title": "Shared Pool usage",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Megabytes",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORASGAS",
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
