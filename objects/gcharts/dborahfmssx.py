class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHFMSSX",
            "title": "FMS: %(DBORAHFMSSX)s - Statistics per execution",
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
                                    "projection": "'Elapsed'::text",
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
                                            "table": "(select timestamp, sum(elapsed_time_delta::real) / 1000000.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where force_matching_signature = '%(DBORAHFMSSX)s' group by timestamp) as foo",
                                            "projection": "'xxx'::text",
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
                    "title": "Buffer gets & disk reads per exec",
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
                                    "projection": "'Gets'::text",
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
                                            "table": "(select timestamp, sum(buffer_gets_delta::real) * 1.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where force_matching_signature = '%(DBORAHFMSSX)s' group by timestamp) as foo",
                                            "projection": "'xxx'::text",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Reads'::text",
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
                                            "table": "(select timestamp, sum(disk_reads_delta::real) * 1.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where force_matching_signature = '%(DBORAHFMSSX)s' group by timestamp) as foo",
                                            "projection": "'xxx'::text",
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
                    "title": "Executions and fetches per exec",
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
                                    "projection": "'Executions'::text",
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
                                            "table": "(select timestamp, sum(executions_delta::real) * 1.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where force_matching_signature = '%(DBORAHFMSSX)s' group by timestamp) as foo",
                                            "projection": "'xxx'::text",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Fetches'::text",
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
                                            "table": "(select timestamp, sum(fetches_delta::real) * 1.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where force_matching_signature = '%(DBORAHFMSSX)s' group by timestamp) as foo",
                                            "projection": "'xxx'::text",
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
                    "title": "Rows processed per exec",
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
                                    "projection": "'Rows processed'::text",
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
                                            "table": "(select timestamp, sum(rows_processed_delta::real) * 1.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where force_matching_signature = '%(DBORAHFMSSX)s' group by timestamp) as foo",
                                            "projection": "'xxx'::text",
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