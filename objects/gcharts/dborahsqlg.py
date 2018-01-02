class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHSQLG",
            "title": "Top SQL - Buffer gets",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of buffer gets per second",
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
                                        "query": "DBORAHHELP",
                                        "variable": "DBORAHELP"
                                    },
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp  as timestamp, sql_id, coalesce(buffer_gets_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp) as foo",
                                            "projection": "sql_id",
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
                                    "projection": "'Captured SQLs'::text",
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
                                            "table": "(select h.timestamp  as timestamp, sql_id, coalesce(buffer_gets_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp) as foo",
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