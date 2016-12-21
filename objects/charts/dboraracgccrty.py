class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACGCCRTY",
            "icon": "bar-chart",
            "title": "Global exchanges between instances - CR blocks - To y",
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
                                    "query": "DBORARACGCCRTY",
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
