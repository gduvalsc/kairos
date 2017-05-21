class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONLCPU",
            "icon": "bar-chart",
            "title": "Logical CPU used",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Logical processors used",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONLCPU",
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
                                    "query": "NMONLCPUALL",
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
