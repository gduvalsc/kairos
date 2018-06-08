class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAWEP",
            "title": "Top wait events - Parallel query",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAWEP$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {
                                        "variable": "DBORAWEV",
                                        "action": "dispchart",
                                        "chart": "DBORACHOOSEWEV"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)