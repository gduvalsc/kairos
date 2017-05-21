class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONTOPMEM",
            "icon": "bar-chart",
            "title": "Top processes consuming memory",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Size",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONTOPMEM",
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
                                    "query": "NMONTOPMEMA",
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
