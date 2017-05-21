class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "SARDWAT",
            "icon": "bar-chart",
            "title": "Disks - Wait time",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "collections": ['SARD'],
            "yaxis": [
                {
                    "title": "Wait time (ms)",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "SARDWAT",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARDWATMAX",
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
