null=None
true=True
false=False

class UserObject(dict):
    def __init__(s):
        object = {
            "id": "SNAPPERWEVOID",
            "title": "Top object ids for event: %(SNAPPERWEVOID)s",
            "subtitle": "",
            "reftime": "SNAPPERREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Number of active sessions",
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
                                        "SNAPPER"
                                    ],
                                    "userfunctions": [
                                        "snappercoeff"
                                    ],
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "SNAPPER, (select snappercoeff() as snappercoeff) as foo",
                                            "projection": "obj_id",
                                            "restriction": "event = '%(SNAPPERWEVOID)s'",
                                            "value": "pthread / 100 /snappercoeff"
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