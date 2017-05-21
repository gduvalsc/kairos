class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASQV",
            "title": "Top SQL - Version count",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of versions",
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
                                        "DBORASQV"
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
                                            "table": "DBORASQV",
                                            "projection": "sqlid",
                                            "restriction": "",
                                            "value": "versioncount"
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
                                        "DBORASQV"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASQV",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "versioncount"
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
