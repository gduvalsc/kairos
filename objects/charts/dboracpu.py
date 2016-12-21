class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORACPU",
            "icon": "bar-chart",
            "title": "CPU usage",
            "subtitle": "",
            "yaxis": [
                {
                    "title": "# per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACPU",
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
