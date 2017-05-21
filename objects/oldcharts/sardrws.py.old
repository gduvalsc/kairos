class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "SARDRWS",
            "icon": "bar-chart",
            "title": "Disks - Reads / Writes",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "collections": ['SARD'],
            "yaxis": [
                {
                    "title": "# of I/Os per second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "SARDRWS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARDRWSMAX",
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
