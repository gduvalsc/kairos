class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAROWS",
            "title": "Read rows",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average number of read rows per second",
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
                                            "restriction": "meet(statistic, '(table fetch|table scan rows)')",
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