class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGDBOVROLLBACKS",
            "title": "Overview  - Rollbacks per database",
            "subtitle": "",
            "reftime": "PGDBREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of rollbacks per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "vkpg_stat_database"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vkpg_stat_database",
                                            "projection": "datname",
                                            "restriction": "",
                                            "value": "xact_rollback"
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
                                    "projection": "label",
                                    "collections": [
                                        "vkpg_stat_database"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vkpg_stat_database",
                                            "projection": "'all databases'::text",
                                            "restriction": "",
                                            "value": "xact_rollback"
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