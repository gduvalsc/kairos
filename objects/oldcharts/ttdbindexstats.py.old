class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "TTDBINDEXSTATS",
            "icon": "bar-chart",
            "title": "DB Index statistics",
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
                                    "query": "TTDBINDEXSTATS",
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
