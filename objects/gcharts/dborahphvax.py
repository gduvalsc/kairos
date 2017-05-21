class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHPHVAX",
            "title": "PHV: %(DBORAHPHVAX)s - Statistics per exec",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Elapsed (sec) per execution",
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
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "apwait_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Concurrency'",
                                    "collections": [
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "ccwait_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'User I/O'",
                                    "collections": [
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "iowait_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Cluster'",
                                    "collections": [
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "clwait_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Cpu'",
                                    "collections": [
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "cpu_time_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
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
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "elapsed_time_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
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
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "buffer_gets_delta * 1.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Reads'",
                                    "collections": [
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "disk_reads_delta * 1.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
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
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "executions_delta * 1.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Fetches'",
                                    "collections": [
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "fetches_delta * 1.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
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
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "plan_hash_value='%(DBORAHPHVAX)s'",
                                            "value": "rows_processed_delta * 1.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
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
