class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORARACGCEPL",
            "title": "Global cache efficiency percentages - Local access",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Local access (%)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "black"
                        },
                        "text": {
                            "fill": "black"
                        }
                    },
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "avg",
                                    "projection": "label",
                                    "collections": [
                                        "DBORARACGCEP"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORARACGCEP",
                                            "projection": "inum",
                                            "restriction": "",
                                            "value": "plocal"
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