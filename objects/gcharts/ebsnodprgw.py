class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EBSNODPRGW",
            "title": "E-Business Suite - Top waiting programs for node: %(EBSNODPRGW)s",
            "subtitle": "",
            "reftime": "EBSREFTIME",
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
                                        "EBS12CM"
                                    ],
                                    "userfunctions": [
                                        "ebscoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "EBS12CM, (select ebscoeff() as ebscoeff) as foo",
                                            "projection": "prg_name",
                                            "restriction": "node_name = '%(EBSNODPRGW)s'::text",
                                            "value": "waitcount * 1.0 / ebscoeff"
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
                                        "EBS12CM"
                                    ],
                                    "userfunctions": [
                                        "ebscoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "EBS12CM, (select ebscoeff() as ebscoeff) as foo",
                                            "projection": "'Waiting executions'::text",
                                            "restriction": "node_name = '%(EBSNODPRGW)s'::text",
                                            "value": "waitcount * 1.0 / ebscoeff"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Estimated wait time (in minutes)",
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
                                    "projection": "label",
                                    "collections": [
                                        "EBS12CM"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "EBS12CM",
                                            "projection": "'Wait time'::text",
                                            "restriction": "node_name = '%(EBSNODPRGW)s'::text",
                                            "value": "wait * 60.0"
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
