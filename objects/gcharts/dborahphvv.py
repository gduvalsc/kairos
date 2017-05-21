class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHPHVV",
            "title": "Top PHV - Version count",
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
                                        "ORAHQS"
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
                                            "table": "ORAHQS",
                                            "projection": "plan_hash_value",
                                            "restriction": "",
                                            "value": "version_count"
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
                                    "projection": "'Captured PHVs'",
                                    "collections": [
                                        "ORAHQS"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "ORAHQS",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "version_count"
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
