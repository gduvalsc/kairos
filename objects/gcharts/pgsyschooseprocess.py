class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSCHOOSEPROCESS",
            "title": "Display metrics for process: %(PGSYSPROCESS)s",
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
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'",
                                            "value": "usr"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'SYS_TIME'",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'",
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
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'",
                                            "value": "rss"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Virtual size'",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'",
                                            "value": "vms"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Text size'",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'",
                                            "value": "texts"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Shared size'",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'",
                                            "value": "shared"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Data size'",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'",
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