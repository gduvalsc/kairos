class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHITD",
            "title": "Cache activity - Default pool - Hit ratio",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Number of buffer gets / reads per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'gets'",
                                    "collections": [
                                        "DBORABUF"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORABUF",
                                            "projection": "'xxx'",
                                            "restriction": "bufpool='D'",
                                            "value": "gets"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'reads'",
                                    "collections": [
                                        "DBORABUF"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORABUF",
                                            "projection": "'xxx'",
                                            "restriction": "bufpool='D'",
                                            "value": "reads"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Hit ratio (%)",
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
                    "minvalue": null,
                    "maxvalue": 101,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'hit ratio'",
                                    "collections": [
                                        "DBORABUF"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORABUF",
                                            "projection": "'xxx'",
                                            "restriction": "bufpool='D'",
                                            "value": "100.0 * (1 - (reads / gets))"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Waits per second",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'write complete waits'",
                                    "collections": [
                                        "DBORABUF"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORABUF",
                                            "projection": "'xxx'",
                                            "restriction": "bufpool='D'",
                                            "value": "writecompletewaits"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'free buffer waits'",
                                    "collections": [
                                        "DBORABUF"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORABUF",
                                            "projection": "'xxx'",
                                            "restriction": "bufpool='D'",
                                            "value": "freewaits"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'buffer busy waits'",
                                    "collections": [
                                        "DBORABUF"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORABUF",
                                            "projection": "'xxx'",
                                            "restriction": "bufpool='D'",
                                            "value": "busywaits"
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
