class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONDISKOV",
            "title": "Disks - Activity overview",
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
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'Read MB/s'::text",
                                    "collections": [
                                        "NMONDISKREAD"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONDISKREAD",
                                            "projection": "'xxx'::text",
                                            "restriction": "",
                                            "value": "value / 1024.0"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Write MB/s'::text",
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
                                            "projection": "'xxx'::text",
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