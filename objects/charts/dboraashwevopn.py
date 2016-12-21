class UserObject(dict):
    def __init__(s):
        if 'DBORAASHWEVOPN' not in kairos: kairos['DBORAASHWEVOPN'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHWEVOPN",
            "icon": "bar-chart",
            "title": "Top SQL operations for event: " + kairos["DBORAASHWEVOPN"],
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
                                    "query": "DBORAASHWEVOPN",
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
