class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONPROCAIO",
            "title": "Asynchronous I/O activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of aio processors /running aios",
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
                                        "NMONPROCAIO"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONPROCAIO",
                                            "projection": "id",
                                            "restriction": "id in ('aioprocs','aiorunning')",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "CPU used by asynchronous I/O (%) of aio processors /running aios",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "NMONPROCAIO"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONPROCAIO",
                                            "projection": "id",
                                            "restriction": "id in ('aiocpu')",
                                            "value": "value"
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