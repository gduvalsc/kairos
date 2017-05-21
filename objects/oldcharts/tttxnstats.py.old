class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "TTTXNSTATS",
            "icon": "bar-chart",
            "title": "Txn statistics",
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
                                    "query": "TTTXNSTATS",
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
