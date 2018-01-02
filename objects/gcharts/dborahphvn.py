class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHPHVN",
            "title": "Top PHV - Rows processed",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of rows per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": {
                                        "query": "DBORAHHELPP",
                                        "variable": "DBORAHELPP"
                                    },
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp as timestamp, plan_hash_value, coalesce(rows_processed_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp) as foo",
                                            "projection": "plan_hash_value",
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
                                    "projection": "'Captured PHVs'::text",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp as timestamp, plan_hash_value, coalesce(rows_processed_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp) as foo",
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
