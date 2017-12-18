class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXADSKOSIOFR",
            "title": "IO requests - Top flash devices",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of IO requests (Flash) per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "EXATOPDSKOSIO"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "EXATOPDSKOSIO",
                                            "projection": "disk",
                                            "restriction": "type like 'F/%'",
                                            "value": "raverage"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "EXATOPDSKOSIO"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "EXATOPDSKOSIO",
                                            "projection": "'Flash device maximum capacity'",
                                            "restriction": "",
                                            "value": "8929.0"
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