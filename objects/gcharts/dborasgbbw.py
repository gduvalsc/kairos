class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASGBBW",
            "title": "Top segments by buffer busy waits",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of waits per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORASGBBW"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASGBBW",
                                            "projection": "owner||' '||objtype||' '||object||' '||subobject",
                                            "restriction": "",
                                            "value": "waits"
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
