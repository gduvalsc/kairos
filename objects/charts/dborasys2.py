class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASYS2",
            "icon": "bar-chart",
            "title": "System statistics",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "CPU used (seconds)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "WSA",
                            "datasets": [
                                {
                                    "query": "DBORASYSCPU",
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
