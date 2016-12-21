class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACGCEPL",
            "icon": "bar-chart",
            "title": "Global cache efficiency percentages - Local access",
            "subtitle": "",
            "collections": ['DBORARACGCEP'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "Local access (%)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACGCEPL",
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
