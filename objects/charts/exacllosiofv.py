class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXACLLOSIOFV",
            "title": "Flash OS IO volume - Top cells",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of megabytes per second",
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
                                    "query": "EXACLLOSIOFV$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "EXACLLOSIOFV$$2",
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