class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "TTSTMTSTATS",
            "icon": "bar-chart",
            "title": "Stmt statistics",
            "subtitle": "",
            "reftime": "TTREFTIME",
            "yaxis": [
                {
                    "title": "# of operations per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "TTSTMTSTATS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
