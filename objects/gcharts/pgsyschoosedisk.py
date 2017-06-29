class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSCHOOSEDISK",
            "title": "Display metrics for disk: %(PGSYSDISK)s",
            "subtitle": "",
            "reftime": "PGSYSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average time (ms) per operation (read or write)",
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
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_disk_io_counters"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average time per read'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "(case when read_count = 0 then 0.0 else read_time * 1.0 / read_count end)"
                                        },
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average time per write'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "(case when write_count = 0 then 0.0 else write_time * 1.0 / write_count end)"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Average volume per operation (read or write)",
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
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_disk_io_counters"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average volume per read'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "(case when read_count = 0 then 0.0 else read_bytes / read_count end)"
                                        },
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average volume per write'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "(case when write_count = 0 then 0.0 else write_bytes / write_count end)"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Throughput",
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
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_disk_io_counters"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average read volume per second'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "read_bytes"
                                        },
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average write volume per second'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "write_bytes"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Throughput expressed in operations per second",
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
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_disk_io_counters"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average read count per second'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "read_count"
                                        },
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average write count per second'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "write_count"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Time spent (ms) on device per second",
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
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_disk_io_counters"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average read time'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "read_time"
                                        },
                                        {
                                            "table": "vpsutil_disk_io_counters",
                                            "projection": "'Average write time'",
                                            "restriction": "disk = '%(PGSYSDISK)s'",
                                            "value": "write_time"
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