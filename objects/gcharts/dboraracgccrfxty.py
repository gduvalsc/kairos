class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORARACGCCRFXTY",
            "title": "Global exchanges between instances - CR blocks - From x to y",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of blocks per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "gray"
                        },
                        "text": {
                            "fill": "gray"
                        }
                    },
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORARACGCTS"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORARACGCTS",
                                            "projection": "'From '||src||' to '||dest",
                                            "restriction": "",
                                            "value": "crblocks"
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