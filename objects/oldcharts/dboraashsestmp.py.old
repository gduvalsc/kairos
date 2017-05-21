class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSESTMP' not in kairos: kairos['DBORAASHSESTMP'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSESTMP",
            "icon": "bar-chart",
            "title": "Temp space allocated for session: " + kairos["DBORAASHSESTMP"],
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "yaxis": [
                {
                    "title": "Size allocated in bytes",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAASHSESTMP",
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
