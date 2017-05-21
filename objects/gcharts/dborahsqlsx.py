class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHSQLSX",
            "title": "SQL request: %(DBORAHSQLSX)s - Statistics per execution",
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
                                            "restriction": "sql_id='%(DBORAHSQLSX)s'",
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
                                            "restriction": "sql_id='%(DBORAHSQLSX)s'",
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
                                            "restriction": "sql_id='%(DBORAHSQLSX)s'",
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
                                            "restriction": "sql_id='%(DBORAHSQLSX)s'",
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
                                            "restriction": "sql_id='%(DBORAHSQLSX)s'",
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
                                            "restriction": "sql_id='%(DBORAHSQLSX)s'",
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