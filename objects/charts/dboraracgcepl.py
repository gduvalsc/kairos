class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORARACGCEPL",
            "title": "Global cache efficiency percentages - Local access",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Local access (%)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "gray"
                        },
                        "text": {
                            "fill": "gray"
                        }
                    },
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACGCEPL$$1",
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