class UserObject(dict):
    def __init__(s):
        object = {
            "id": "SNAPPERSQL",
            "title": "Top SQL requests",
            "subtitle": "",
            "reftime": "SNAPPERREFTIME",
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
                                        "SNAPPER"
                                    ],
                                    "userfunctions": [
                                        "snappercoeff"
                                    ],
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "SNAPPER",
                                            "projection": "sql_id",
                                            "restriction": "sql_id != ''",
                                            "value": "pthread / 100 / snappercoeff()"
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