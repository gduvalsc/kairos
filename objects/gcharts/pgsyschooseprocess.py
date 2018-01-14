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
                                            "projection": "'USER_TIME'::text",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text",
                                            "value": "usr::real"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'SYS_TIME'::text",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text",
                                            "value": "sys::real"
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
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text",
                                            "value": "rss::real"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Virtual size'::text",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text",
                                            "value": "vms::real"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Text size'::text",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text",
                                            "value": "texts::real"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Shared size'::text",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text",
                                            "value": "shared::real"
                                        },
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'Data size'::text",
                                            "restriction": "pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text",
                                            "value": "datas::real"
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