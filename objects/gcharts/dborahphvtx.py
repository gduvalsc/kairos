class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHPHVTX",
            "title": "PHV: %(DBORAHPHVTX)s - Statistics per exec",
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
                                            "restriction": "plan_hash_value='%(DBORAHPHVTX)s'",
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
                                            "restriction": "plan_hash_value='%(DBORAHPHVTX)s'",
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
                                            "restriction": "plan_hash_value='%(DBORAHPHVTX)s'",
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
                                            "restriction": "plan_hash_value='%(DBORAHPHVTX)s'",
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
                                            "restriction": "plan_hash_value='%(DBORAHPHVTX)s'",
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
                                            "restriction": "plan_hash_value='%(DBORAHPHVTX)s'",
                                            "value": "elapsed_time_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end)"
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
