class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGDBSBACKENDS",
            "title": "Activity - All backends",
            "subtitle": "",
            "reftime": "PGDBSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Number of backends",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "vkpg_stat_activity"
                                    ],
                                    "userfunctions": [
                                        "pgdbscoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vkpg_stat_activity",
                                            "projection": "datname",
                                            "restriction": "",
                                            "value": "1.0 / pgdbscoeff(cast(snap_frequency as integer))"
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