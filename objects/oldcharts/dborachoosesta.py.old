class UserObject(dict):
    def __init__(s):
        if 'DBORASTA' not in kairos: kairos['DBORASTA'] = ''
        object = {
            "type": "chart",
            "id": "DBORACHOOSESTA",
            "icon": "bar-chart",
            "title": "Display statistic: " + kairos["DBORASTA"],
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of units each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACHOOSESTA",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
