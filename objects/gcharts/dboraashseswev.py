class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAASHSESWEV",
            "title": "Top wait events for session: %(DBORAASHSESWEV)s",
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
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
                                        "ORAHAS"
                                    ],
                                    "userfunctions": [
                                        "ashcoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHAS",
                                            "projection": "case when event = '' then 'on cpu' when event != '' then event end",
                                            "restriction": "session_id||' - '||program = '%(DBORAASHSESWEV)s'",
                                            "value": "kairos_count * 1.0 /ashcoeff()"
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