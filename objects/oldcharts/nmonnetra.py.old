class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONNETRA",
            "icon": "bar-chart",
            "title": "Network - Read activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Volume (MB/s)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONNETRA",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONNETRAA",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
