class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAPGA",
            "title": "PGA Usage",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Memory / Workarea (manuel + auto) allocated (Megabytes)",
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
                                    "projection": "'Workarea (Manual + Auto) allocated'",
                                    "collections": [
                                        "DBORAPGA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAPGA",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "memused"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Memory other allocated'",
                                    "collections": [
                                        "DBORAPGA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAPGA",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "memalloc - memused"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'Memory allocated'",
                                    "collections": [
                                        "DBORAPGA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAPGA",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "memalloc"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'PGA aggregate target'",
                                    "collections": [
                                        "DBORAPGA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAPGA",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "aggrtarget"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "One pass or Multi pass execs during snap",
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
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'One pass execs'",
                                    "collections": [
                                        "DBORAPGC"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select c.timestamp timestamp, execs1 * elapsed value from DBORAPGC c, DBORAMISC m where c.timestamp = m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Multi pass execs'",
                                    "collections": [
                                        "DBORAPGC"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select c.timestamp timestamp, execs2 * elapsed value from DBORAPGC c, DBORAMISC m where c.timestamp = m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
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