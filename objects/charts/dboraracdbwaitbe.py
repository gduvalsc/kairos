class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACDBWAITBE",
            "icon": "bar-chart",
            "title": "Background wait events",
            "subtitle": "",
            "collections": ['DBORARACTTBE'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACDBWAITBEPE",
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
                                    "query": "DBORARACDBWAITBE",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
