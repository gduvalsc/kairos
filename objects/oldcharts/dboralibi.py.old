class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORALIBI",
            "icon": "bar-chart",
            "title": "Library cache invalidations",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Average number of invalidations per second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORALIBI",
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
                                    "query": "DBORASUMLIBI",
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
