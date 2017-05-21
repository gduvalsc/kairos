class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONDISKOV",
            "icon": "bar-chart",
            "title": "Disks - Activity overview",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Volume (MB/s)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONDISKOVR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "NMONDISKOVW",
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
