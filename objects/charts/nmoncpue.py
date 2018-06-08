class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONCPUE",
            "title": "LPAR CPU utilization vs Entitled capacity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Entitled capacity (%)",
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
                                    "query": "NMONCPUE$$1",
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