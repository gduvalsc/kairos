class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONDISKBSY",
            "icon": "bar-chart",
            "title": "Disks - Busy rate",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Busy (%)",
                    "scaling": "linear",
                    "minvalue": 0,
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONDISKBSY",
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
                                    "query": "NMONDISKBSYMAX",
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
