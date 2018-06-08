class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORARACGCEPD",
            "title": "Global cache efficiency percentages - Disk access",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Disk access (%)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "black"
                        },
                        "text": {
                            "fill": "black"
                        }
                    },
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACGCEPD$$1",
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