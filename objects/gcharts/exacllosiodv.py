class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EXACLLOSIODV",
            "title": "Hard disk OS IO volume - Top cells",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of megabytes per second",
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
                                        "EXATOPCLLOSIO"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "EXATOPCLLOSIO",
                                            "projection": "type || ' - ' || cell",
                                            "restriction": "type like 'H/%'",
                                            "value": "vaverage"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "EXATOPCLLOSIO"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "EXATOPCLLOSIO",
                                            "projection": "'Flash disk maximum capacity for cell'",
                                            "restriction": "",
                                            "value": "1332.0"
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