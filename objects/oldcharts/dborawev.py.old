class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAWEV",
            "icon": "bar-chart",
            "title": "Top wait events",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAWEV",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {
                                        "action": "dispchart",
                                        "chart": "DBORACHOOSEWEV",
                                        "variable": "DBORAWEV"
                                    }
                                },
                            ]
                        },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
