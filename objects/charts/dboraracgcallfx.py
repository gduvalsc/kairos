class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACGCALLFX",
            "icon": "bar-chart",
            "title": "Global exchanges between instances - All blocks - From x",
            "subtitle": "",
            "collections": ['DBORARACGCTS'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": " # of blocks per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACGCALLFX",
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
