class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAASHSESOPN",
            "title": "Top SQL operations for session: %(DBORAASHSESOPN)s",
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
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORAASHSESOPN$$1",
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