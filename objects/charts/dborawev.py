class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAWEV",
            "title": "Top wait events",
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
                                    "query": "DBORAWEV$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {
                                        "action": "dispchart",
                                        "chart": "DBORACHOOSEWEV",
                                        "variable": "DBORAWEV"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)