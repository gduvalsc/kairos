class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSQLTMP' not in kairos: kairos['DBORAASHSQLTMP'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSQLTMP",
            "icon": "bar-chart",
            "title": "Temp space allocated for SQL request: " + kairos["DBORAASHSQLTMP"],
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
                                    "query": "DBORAASHSQLTMP",
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
