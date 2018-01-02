class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXADSKOSIOFU",
            "title": "IO utilization - Top flash devices",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Utilization (%)",
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
                                    "query": "EXADSKOSIOFU$$1",
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