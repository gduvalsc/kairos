class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAIOA",
            "icon": "bar-chart",
            "title": "I/O overall activity",
            "subtitle": "",
            "yaxis": [
                {
                    "title": "Volume per second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAIOAV",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        }
                    ]
                },
                {
                    "title": "# of I/O requests per second",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAIOAR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
