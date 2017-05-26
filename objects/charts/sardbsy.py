class UserObject(dict):
    def __init__(s):
        object = {
            "id": "SARDBSY",
            "title": "Disks - Usage",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Usage (%)",
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
                                    "query": "SARDBSY$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARDBSY$$2",
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