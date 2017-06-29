class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSCHOOSEFAMILY",
            "title": "Display metrics for family: %(PGSYSFAMILY)s",
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
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'",
                                            "value": "usr"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'SYS_TIME'",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'",
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
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'",
                                            "value": "rss"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Virtual size'",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'",
                                            "value": "vms"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Text size'",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'",
                                            "value": "texts"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Shared size'",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'",
                                            "value": "shared"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Data size'",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'",
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