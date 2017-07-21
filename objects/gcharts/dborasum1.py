class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASUM1",
            "title": "DB CPU & Wait - Gets - Reads - Redo",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "black"
                        },
                        "text": {
                            "fill": "black"
                        }
                    },
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'wait events'",
                                    "collections": [
                                        "DBORAWEV"
                                    ],
                                    "userfunctions": [
                                        "idlewev",
                                        "pxwev"
                                    ],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEV",
                                            "projection": "event",
                                            "restriction": "not idlewev(event) and not pxwev(event)",
                                            "value": "time"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORASTA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASTA",
                                            "projection": "statistic",
                                            "restriction": "statistic='CPU used by this session'",
                                            "value": "value / 100.0"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of logical reads per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "darkgreen"
                        },
                        "text": {
                            "fill": "darkgreen"
                        }
                    },
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
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASTA",
                                            "projection": "statistic",
                                            "restriction": "statistic='session logical reads'",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of physical reads per second",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "red"
                        },
                        "text": {
                            "fill": "red"
                        }
                    },
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
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASTA",
                                            "projection": "statistic",
                                            "restriction": "statistic='physical reads'",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of redo bytes per second",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "blue"
                        },
                        "text": {
                            "fill": "blue"
                        }
                    },
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
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASTA",
                                            "projection": "statistic",
                                            "restriction": "statistic='redo size'",
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