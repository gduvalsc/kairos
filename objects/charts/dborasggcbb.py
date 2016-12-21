class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASGGCBB",
            "icon": "bar-chart",
            "title": "Top segments by global cache buffer busy waits",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of waits per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORASGGCBB",
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
