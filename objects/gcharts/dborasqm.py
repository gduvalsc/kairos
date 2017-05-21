class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASQM",
            "title": "Top SQL - Shared memory",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "size in bytes",
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
                                        "DBORASQM"
                                    ],
                                    "userfunctions": [],
                                    "info": {
                                        "variable": "DBORAHELP",
                                        "query": "DBORAHELP"
                                    },
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASQM",
                                            "projection": "sqlid",
                                            "restriction": "",
                                            "value": "sharedmem"
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
                                    "projection": "'Captured SQLs'",
                                    "collections": [
                                        "DBORASQM"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASQM",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "sharedmem"
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
