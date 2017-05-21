class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "SARDSVC",
            "icon": "bar-chart",
            "title": "Disks - Service time",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "collections": ['SARD'],
            "yaxis": [
                {
                    "title": "Service time (ms)",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "SARDSVC",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARDSVCMAX",
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
