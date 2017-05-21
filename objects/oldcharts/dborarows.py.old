class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAROWS",
            "icon": "bar-chart",
            "title": "Read rows",
            "subtitle": "",
            "yaxis": [
                {
                    "title": "Average number of read rows per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAROWS",
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
