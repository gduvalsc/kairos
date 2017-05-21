class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONDISKWA",
            "title": "Disks - Write activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Volume (MB/s)",
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
                                        "NMONDISKWRITE"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONDISKWRITE",
                                            "projection": "id",
                                            "restriction": "",
                                            "value": "value / 1024.0"
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
                                    "projection": "'Write MB/s'",
                                    "collections": [
                                        "NMONDISKWRITE"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONDISKWRITE",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value / 1024.0"
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