class UserObject(dict):
    def __init__(s):
        object = {
            "id": "TTSQLTOPXT",
            "title": "Top SQL by execution time",
            "subtitle": "",
            "reftime": "TTREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Duration in ms",
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
                                    "query": "TTSQLTOPXT$$1",
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