class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASGA",
            "title": "SGA Usage",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Megabytes",
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
                                        "DBORASGA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASGA",
                                            "projection": "coalesce(pool, '')||' '||name",
                                            "restriction": "",
                                            "value": "size"
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