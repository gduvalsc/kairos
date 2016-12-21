class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONJFSFILE",
            "icon": "bar-chart",
            "title": "Filespace - Occupation rate",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Occupation rate (%)",
                    "scaling": "linear",
                    "maxvalue": 110,
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONJFSFILE",
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
