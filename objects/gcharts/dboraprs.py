class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAPRS",
            "title": "SQL activity - Parsing",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORASTA"
                                    ],
                                    "userfunctions": [
                                        "meet"
                                    ],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASTA",
                                            "projection": "statistic",
                                            "restriction": "meet(statistic, '(execute|parse count|session cursor)')",
                                            "value": "value"
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