class UserObject(dict):
    def __init__(s):
        object = {
            "id": "SARDBSY",
            "title": "Disks - Usage",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Usage (%)",
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
                                            "value": "busy"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "max",
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
                                            "projection": "'Max (%) all disks'::text",
                                            "restriction": "",
                                            "value": "busy"
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