class UserObject(dict):
    def __init__(s):
        object = {
            "id": "BOUSRREQ",
            "title": "Business Objects - Top requests for user: %(BOUSRREQ)s",
            "subtitle": "",
            "reftime": "BOREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average number of concurrent sessions per unit of time",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "text": {
                            "fill": "red"
                        },
                        "line": {
                            "stroke": "red"
                        }
                    },
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "BO"
                                    ],
                                    "userfunctions": [
                                        "bocoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "BO",
                                            "projection": "report||' - '||event_id||' (duration: '||duration||')'",
                                            "restriction": "user_name = '%(BOUSRREQ)s'",
                                            "value": "executecount * 1.0 / bocoeff()"
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
                                    "projection": "'All requests'",
                                    "collections": [
                                        "BO"
                                    ],
                                    "userfunctions": [
                                        "bocoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "BO",
                                            "projection": "'xxx'",
                                            "restriction": "user_name = '%(BOUSRREQ)s'",
                                            "value": "executecount * 1.0 / bocoeff()"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Estimated response time (in minutes)",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {
                        "text": {
                            "fill": "blue"
                        },
                        "line": {
                            "stroke": "blue"
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
                                    "projection": "'Response time'",
                                    "collections": [
                                        "BO"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "BO",
                                            "projection": "'xxx'",
                                            "restriction": "user_name = '%(BOUSRREQ)s'",
                                            "value": "duration / 60.0"
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