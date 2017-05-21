class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORALIBR",
            "icon": "bar-chart",
            "title": "Library cache reloads",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Average number of reloads per second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORALIBR",
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
                                    "query": "DBORASUMLIBR",
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
