class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORARACGCCUFX",
            "title": "Global exchanges between instances - Current blocks - From x",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of blocks per second",
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
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACGCCUFX$$1",
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