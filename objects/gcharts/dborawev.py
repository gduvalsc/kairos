class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAWEV",
            "title": "Top wait events",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
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
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEV"
                                    ],
                                    "userfunctions": [
                                        "idlewev",
                                        "pxwev"
                                    ],
                                    "onclick": {
                                        "action": "dispchart",
                                        "chart": "DBORACHOOSEWEV",
                                        "variable": "DBORAWEV"
                                    },
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEV",
                                            "projection": "event",
                                            "restriction": "not idlewev(event) and not pxwev(event)",
                                            "value": "time"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
