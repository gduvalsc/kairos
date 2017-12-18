class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXADSKOSIODV",
            "title": "IO volume - Top hard disks",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of megabytes (Disk) per second",
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
                                            "restriction": "type like 'H/%'",
                                            "value": "vaverage"
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
                                            "projection": "'Hard disk maximum capacity for disk'",
                                            "restriction": "",
                                            "value": "111.0"
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