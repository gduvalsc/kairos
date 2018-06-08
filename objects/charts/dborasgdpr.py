class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASGDPR",
            "title": "Top segments by direct physical reads",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of blocks / physical reads per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORASGDPR$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASGDPR$$2",
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