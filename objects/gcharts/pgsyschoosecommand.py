class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSCHOOSECOMMAND",
            "title": "Display metrics for command: %(PGSYSCOMMAND)s",
            "subtitle": "",
            "reftime": "PGSYSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "CPU Usage",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_processes"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'USER_TIME'",
                                            "restriction": "pname = '%(PGSYSCOMMAND)s'",
                                            "value": "usr"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'SYS_TIME'",
                                            "restriction": "pname = '%(PGSYSCOMMAND)s'",
                                            "value": "sys"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Memory Usage",
                    "position": "RIGHT",
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
                                        "vpsutil_processes"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Resident size'",
                                            "restriction": "pname = '%(PGSYSCOMMAND)s'",
                                            "value": "rss"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Virtual size'",
                                            "restriction": "pname = '%(PGSYSCOMMAND)s'",
                                            "value": "vms"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Text size'",
                                            "restriction": "pname = '%(PGSYSCOMMAND)s'",
                                            "value": "texts"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Shared size'",
                                            "restriction": "pname = '%(PGSYSCOMMAND)s'",
                                            "value": "shared"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Data size'",
                                            "restriction": "pname = '%(PGSYSCOMMAND)s'",
                                            "value": "datas"
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