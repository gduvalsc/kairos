class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASCAN",
            "title": "Table scans",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average number of table scans per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "SC",
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
                                            "restriction": "meet(statistic, '(table scans)')",
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
