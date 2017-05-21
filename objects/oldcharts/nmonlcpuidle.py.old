class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONLCPUIDLE",
            "icon": "bar-chart",
            "title": "Logical CPU idle",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Idle logical processors",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONLCPUIDLE",
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
                                    "query": "NMONLCPUIDLEALL",
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
