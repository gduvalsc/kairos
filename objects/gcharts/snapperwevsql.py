null=None
true=True
false=False

class UserObject(dict):
    def __init__(self):
        object = {
            "id": "SNAPPERWEVSQL",
            "title": "Top SQL requests for event: %(SNAPPERWEVSQL)s",
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
                                            "projection": "sql_id",
                                            "restriction": "event = '%(SNAPPERWEVSQL)s'",
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
        super(UserObject, self).__init__(**object)
