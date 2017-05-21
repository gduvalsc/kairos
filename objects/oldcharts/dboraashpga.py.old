class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAASHPGA",
            "icon": "bar-chart",
            "title": "PGA allocated - Top sessions",
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "yaxis": [
                {
                    "title": " Size allocated in bytes",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORAASHPGA",
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
                                    "query": "DBORAASHSUMPGA",
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
