class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAPRS",
            "icon": "bar-chart",
            "title": "SQL activity - Parsing",
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
                                    "query": "DBORAPRS",
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
