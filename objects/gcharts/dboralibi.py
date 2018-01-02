class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORALIBI",
            "title": "Library cache invalidations",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average number of invalidations per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORALIB"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORALIB",
                                            "projection": "item",
                                            "restriction": "",
                                            "value": "invalidations"
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
                                    "projection": "'Invalidations'::text",
                                    "collections": [
                                        "DBORALIB"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORALIB",
                                            "projection": "'xxx'::text",
                                            "restriction": "",
                                            "value": "invalidations"
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