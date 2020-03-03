class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGDBOVFETCHES",
            "title": "Overview  - Fetched rows per database",
            "subtitle": "",
            "reftime": "PGDBREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of fetched rows per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
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
                                            "value": "tup_fetched"
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
                                            "value": "tup_fetched"
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
