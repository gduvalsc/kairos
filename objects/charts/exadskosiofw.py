class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXADSKOSIOFW",
            "title": "IO wait time - Top flash devices",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Wait time (ms)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "EXADSKOSIOFW$$1",
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