class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORACHG",
            "icon": "bar-chart",
            "title": "Logical & Physical writes",
            "subtitle": "",
            "yaxis": [
                {
                    "title": "# of units each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACHG",
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
