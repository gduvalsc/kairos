class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACGCALL",
            "icon": "bar-chart",
            "title": "Global exchanges between instances - Current blocks - CR blocks",
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
                                    "query": "DBORARACGCALLCU",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORARACGCALLCR",
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
