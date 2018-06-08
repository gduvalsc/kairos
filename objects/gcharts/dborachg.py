class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORACHG",
            "title": "Logical & Physical writes",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of units each second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORASTA"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASTA",
                                            "projection": "statistic",
                                            "restriction": "statistic in ('consistent changes','db block changes','physical writes','physical writes direct','physical writes direct (lob)','lob writes','physical writes from cache','physical write IO requests')",
                                            "value": "value"
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