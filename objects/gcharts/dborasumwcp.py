class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASUMWCP",
            "title": "DB CPU & Wait classes",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "P",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEC"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEC",
                                            "projection": "eclass",
                                            "restriction": "eclass not in ('DB CPU')",
                                            "value": "time"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'DB CPU'",
                                    "collections": [
                                        "DBORATMS"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORATMS",
                                            "projection": "statistic",
                                            "restriction": "statistic='DB CPU'",
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
