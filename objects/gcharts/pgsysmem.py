class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSMEM",
            "title": "Memory usage",
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
                                        "vpsutil_virt_memory"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Total size'::text",
                                            "restriction": "",
                                            "value": "total"
                                        },
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Available size'::text",
                                            "restriction": "",
                                            "value": "available"
                                        },
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Used size'::text",
                                            "restriction": "",
                                            "value": "used"
                                        },
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Free size'::text",
                                            "restriction": "",
                                            "value": "free"
                                        },
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Active size'::text",
                                            "restriction": "",
                                            "value": "active"
                                        },
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Inactive size'::text",
                                            "restriction": "",
                                            "value": "inactive"
                                        },
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Buffers size'::text",
                                            "restriction": "",
                                            "value": "buffers"
                                        },
                                        {
                                            "table": "vpsutil_virt_memory",
                                            "projection": "'Cached size'::text",
                                            "restriction": "",
                                            "value": "cached"
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