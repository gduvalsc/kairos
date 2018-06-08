class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXACLLOSIOFR",
            "title": "Flash OS IO requests - Top cells",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of IO requests per second",
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
                                    "query": "EXACLLOSIOFR$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "EXACLLOSIOFR$$2",
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