class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSESOPN' not in kairos: kairos['DBORAASHSESOPN'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSESOPN",
            "icon": "bar-chart",
            "title": "Top SQL operations for session: " + kairos["DBORAASHSESOPN"],
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "yaxis": [
                {
                    "title": "Number of active sessions",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORAASHSESOPN",
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
