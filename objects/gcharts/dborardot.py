class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORARDOT",
            "title": "Log file sync vs Redo write time vs Log file parallel write per operation",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Time (ms)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'redo write time'",
                                    "collections": [
                                        "DBORASTA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select x.timestamp timestamp, 10.0 * x.value / y. value value from DBORASTA x, DBORASTA y where x.statistic='redo write time' and y.statistic='redo writes' and x.timestamp = y.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEV"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEV",
                                            "projection": "event",
                                            "restriction": "event='log file sync'",
                                            "value": "1000.0 * time / count"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEB"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEB",
                                            "projection": "event",
                                            "restriction": "event='log file parallel write'",
                                            "value": "1000.0 * time / count"
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
