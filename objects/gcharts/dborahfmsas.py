class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHFMSAS",
            "title": "FMS: %(DBORAHFMSAS)s - Statistics per second",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Elapsed (sec) per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'Application'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, apwait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Concurrency'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, ccwait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'User I/O'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, iowait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Cluster'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, clwait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Cpu'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, cpu_time_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
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
                                    "projection": "'Elapsed'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, elapsed_time_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                                {
                    "title": "Buffer gets & disk reads per second",
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
                                    "projection": "'Gets'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, buffer_gets_delta * 1.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Reads'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, disk_reads_delta * 1.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Executions and fetches per second",
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
                                    "projection": "'Executions'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, executions_delta * 1.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Fetches'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, fetches_delta * 1.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Rows processed per second",
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
                                    "projection": "'Rows processed'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, rows_processed_delta * 1.0 / m.elapsed value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSAS)s' and h.timestamp=m.timestamp)",
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
