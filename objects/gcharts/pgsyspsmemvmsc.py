class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSPSMEMVMSC",
            "title": "Top commands - Virtual memory size",
            "subtitle": "",
            "reftime": "PGSYSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Memory size",
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
                                    "onclick": {
                                        "variable": "PGSYSCOMMAND",
                                        "chart": "PGSYSCHOOSECOMMAND",
                                        "action": "dispchart"
                                    },
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "pname",
                                            "restriction": "",
                                            "value": "vms"
                                        }
                                    ]
                                }
                            ]
                        },
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
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_processes",
                                            "projection": "'All commands'",
                                            "restriction": "",
                                            "value": "vms"
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