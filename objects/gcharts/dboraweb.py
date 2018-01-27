class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAWEB",
            "title": "Top background wait events",
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
                                        "DBORAWEB"
                                    ],
                                    "userfunctions": [
                                        "idlewev",
                                        "pxwev"
                                    ],
                                    "onclick": {
                                        "action": "dispchart",
                                        "variable": "DBORAWEB",
                                        "chart": "DBORACHOOSEWEB"
                                    },
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEB",
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