class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORACHOOSEWEH",
            "title": "Display histogram for event: %(DBORAWEH)s",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Number of operations per sec",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAWEH"
                                    ],
                                    "userfunctions": [],
                                    "onclick": {},
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORAWEH",
                                            "projection": "bucket",
                                            "restriction": "event='%(DBORAWEH)s'",
                                            "value": "count"
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