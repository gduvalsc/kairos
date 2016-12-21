class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORATBSRT",
            "icon": "bar-chart",
            "title": "Tablespace read times",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Read time (s) per tablespace per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORATBSRT",
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
