class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONCPUV",
            "icon": "bar-chart",
            "title": "LPAR CPU utilization vs Virtual capacity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Virtual capacity (%)",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONCPUV",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        }
                    ]
                },
                {
                    "title": "Run queue",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONCPUR",
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
