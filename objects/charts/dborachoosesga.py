class UserObject(dict):
    def __init__(s):
        if 'DBORASGA' not in kairos: kairos['DBORASGA'] = ''
        object = {
            "type": "chart",
            "id": "DBORACHOOSESGA",
            "icon": "bar-chart",
            "title": "Display SGA part: " + kairos["DBORASGA"],
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Megabytes",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACHOOSESGA",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
