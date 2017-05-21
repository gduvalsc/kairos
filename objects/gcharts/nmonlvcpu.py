class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONLVCPU",
            "title": "Logical vs Virtual percentages",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "%",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "avg",
                                    "projection": "'Virtual usr+sys+idle %'",
                                    "collections": [
                                        "NMONLPAR"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select timestamp, sum(value) value from NMONLPAR where id in ('VP_User%', 'VP_Sys%', 'VP_Idle%') group by timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "avg",
                                    "projection": "'Virtual usr+sys %'",
                                    "collections": [
                                        "NMONLPAR"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select timestamp, sum(value) value from NMONLPAR where id in ('VP_User%', 'VP_Sys%') group by timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "avg",
                                    "projection": "'Logical CPU (computation 1) %'",
                                    "collections": [
                                        "NMONCPU"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONCPU",
                                            "projection": "'xxx'",
                                            "restriction": "id = 'ALL'",
                                            "value": "user + sys"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "avg",
                                    "projection": "'Logical CPU (computation 2) %'",
                                    "collections": [
                                        "NMONCPU"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select timestamp, sum(user + sys) / count(cpus) value from NMONCPU where id != 'ALL' group by timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
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