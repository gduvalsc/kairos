class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASQLNET",
            "icon": "bar-chart",
            "title": "SQL*Net traffic - Volume - Roundtrips",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Kbytes per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "CC",
                            "datasets": [
                                {
                                    "query": "DBORANETV",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                    ]
                },
                {
                    "title": "# of roundtrips per second",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORANETR",
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
