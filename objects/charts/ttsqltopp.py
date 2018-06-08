class UserObject(dict):
    def __init__(s):
        object = {
            "id": "TTSQLTOPP",
            "title": "Top SQL by prepares",
            "subtitle": "",
            "reftime": "TTREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of prepares per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "TTSQLTOPP$$1",
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