class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONCPUOV",
            "icon": "bar-chart",
            "title": "LPAR CPU overview",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Number of CPUs",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONCPUOV",
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
