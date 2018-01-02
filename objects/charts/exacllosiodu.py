class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXACLLOSIODU",
            "title": "Hard disk OS IO utilization - Top cells",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "% utilization",
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
                                    "query": "EXACLLOSIODU$$1",
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