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
                                            "projection": "'USER_TIME'::text",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'::text",
                                            "value": "usr"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'SYS_TIME'::text",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'::text",
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
                                            "projection": "'Resident size'::text",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'::text",
                                            "value": "rss"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Virtual size'::text",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'::text",
                                            "value": "vms"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Text size'::text",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'::text",
                                            "value": "texts"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Shared size'::text",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'::text",
                                            "value": "shared"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Data size'::text",
                                            "restriction": "cmdline = '%(PGSYSFAMILY)s'::text",
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