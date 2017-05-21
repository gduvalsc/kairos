class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASUMWCP",
            "icon": "bar-chart",
            "title": "DB CPU & Wait classes",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "renderers": [
                        {
                            "type": "P",
                            "datasets": [
                                {
                                    "query": "DBORAWAITCLASSES",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORADBCPU",
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
