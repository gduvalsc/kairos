class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGDBSABACKENDS",
            "title": "Activity - Active backends",
            "subtitle": "",
            "reftime": "PGDBSREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Number of backends",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "PGDBSABACKENDS$$1",
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