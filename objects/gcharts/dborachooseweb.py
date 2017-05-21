class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORACHOOSEWEB",
            "title": "Display background event: %(DBORAWEB)s",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average time per operation (ms)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "red"
                        },
                        "text": {
                            "fill": "red"
                        }
                    },
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "avg",
                                    "projection": "'average time (ms)'",
                                    "collections": [
                                        "DBORAWEB"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEB",
                                            "projection": "event",
                                            "restriction": "event='%(DBORAWEB)s'",
                                            "value": "1000.0 * time / count"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Number of operations - Timeouts per sec",
                    "position": "RIGHT",
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
                                    "projection": "'number of operations/sec'",
                                    "collections": [
                                        "DBORAWEB"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEB",
                                            "projection": "event",
                                            "restriction": "event='%(DBORAWEB)s'",
                                            "value": "count"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'number of timeouts/sec'",
                                    "collections": [
                                        "DBORAWEB"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEB",
                                            "projection": "event",
                                            "restriction": "event='%(DBORAWEB)s'",
                                            "value": "timeouts"
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
