null=None
true=True
false=False

class UserObject(dict):
    def __init__(self):
        object = {
            "id": "DBORAASHSES",
            "title": "Top foreground sessions",
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Number of active sessions",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "WA",
                            "datasets": [
                                {
                                    "query": "DBORAASHSES$$1",
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
        super(UserObject, self).__init__(**object)
