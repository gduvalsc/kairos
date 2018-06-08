class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAWEVP",
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
                            "type": "P",
                            "datasets": [
                                {
                                    "query": "DBORAWEVP$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {
                                        "action": "dispchart",
                                        "variable": "DBORAWEV",
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