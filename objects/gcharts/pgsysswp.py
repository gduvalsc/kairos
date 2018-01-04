class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSSWP",
            "title": "Swapping activity",
            "subtitle": "",
            "reftime": "PGSYSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Size",
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
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_swap_memory"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_swap_memory",
                                            "projection": "'Total size'::text",
                                            "restriction": "",
                                            "value": "total"
                                        },
                                        {
                                            "table": "vpsutil_swap_memory",
                                            "projection": "'Used size'::text",
                                            "restriction": "",
                                            "value": "used"
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
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_swap_memory"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_swap_memory",
                                            "projection": "'Swap in'::text",
                                            "restriction": "",
                                            "value": "sin"
                                        },
                                        {
                                            "table": "vpsutil_swap_memory",
                                            "projection": "'Swap out'::text",
                                            "restriction": "",
                                            "value": "sout"
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