class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAASHPDBSQL",
            "title": "Top SQL requests - %(DBORAASHPDBSQL)s",
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Number of active sessions",
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
                                    "projection": "label",
                                    "collections": [
                                        "ORAHAS"
                                    ],
                                    "userfunctions": [
                                        "ashcoeff"
                                    ],
                                    "info": {
                                        "variable": "DBORAHELP",
                                        "query": "DBORAHHELP"
                                    },
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHAS, (select ashcoeff() as ashcoeff) as foo",
                                            "projection": "sql_id",
                                            "restriction": "session_type = 'FOREGROUND' and sql_id != '' and con_name = '%(DBORAASHPDBSQL)s'",
                                            "value": "kairos_count * 1.0 /ashcoeff"
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