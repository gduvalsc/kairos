class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASUME2",
            "icon": "bar-chart",
            "title": "DB Time Model",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "WA",
                            "datasets": [
                                {
                                    "query": "DBORATIMEMODEL",
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
