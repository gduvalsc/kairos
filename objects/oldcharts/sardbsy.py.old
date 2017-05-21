class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "SARDBSY",
            "icon": "bar-chart",
            "title": "Disks - Usage",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "collections": ['SARD'],
            "yaxis": [
                {
                    "title": "Usage (%)",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "SARDBSY",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARDBSYMAX",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        },
                    ]
                },
            ],
        }
        super(UserObject, s).__init__(**object)
