class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORACOM",
            "icon": "bar-chart",
            "title": "Transactional activity",
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
                                    "query": "DBORACOM",
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
