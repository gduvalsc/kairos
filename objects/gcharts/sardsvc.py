class UserObject(dict):
    def __init__(s):
        object = {
            "id": "SARDSVC",
            "title": "Disks - Service time",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Service time (ms)",
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
                                        "SARD"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "SARD",
                                            "projection": "device",
                                            "restriction": "",
                                            "value": "avserv"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "max",
                                    "projection": "'Max service time (all disks)'",
                                    "collections": [
                                        "SARD"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "SARD",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "avserv"
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