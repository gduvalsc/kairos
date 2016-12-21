class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONDISKRA",
            "icon": "bar-chart",
            "title": "Disks - Read activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Volume (MB/s)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONDISKRA",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONDISKOVR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
