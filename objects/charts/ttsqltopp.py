class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "TTSQLTOPP",
            "icon": "bar-chart",
            "title": "Top SQL by preparations",
            "subtitle": "",
            "reftime": "TTREFTIME",
            "yaxis": [
                {
                    "title": "# of prepares per second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "TTSQLTOPP",
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
