class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORACHOOSEBUFPOOL",
            "title": "%(DBORABUFPOOL)s buffer pool advisory",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Estimated pysical reads factor",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "DBORABPA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORABPA",
                                            "projection": "sizefactor",
                                            "restriction": "bufpool='%(DBORABUFPOOL)s'",
                                            "value": "estphysreadsfactor"
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