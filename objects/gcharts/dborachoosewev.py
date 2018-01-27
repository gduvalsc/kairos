class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORACHOOSEWEV",
            "title": "Display foreground event: %(DBORAWEV)s",
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
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEV"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEV",
                                            "projection": "'average time (ms)'",
                                            "restriction": "event='%(DBORAWEV)s'",
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
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEV"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEV",
                                            "projection": "'number of operations/sec'",
                                            "restriction": "event='%(DBORAWEV)s'",
                                            "value": "count"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEV"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEV",
                                            "projection": "'number of timeouts/sec'",
                                            "restriction": "event='%(DBORAWEV)s'",
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