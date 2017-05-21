class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONLCPUIDLE",
            "title": "Idle logical CPU",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Idle logical processors",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONLCPUIDLE$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONLCPUIDLE$$2",
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