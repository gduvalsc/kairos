class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASGRLW",
            "title": "Top segments by row lock waits",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of waits per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORASGRLW$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)