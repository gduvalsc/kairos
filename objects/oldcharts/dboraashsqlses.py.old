class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSQLSES' not in kairos: kairos['DBORAASHSQLSES'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSQLSES",
            "icon": "bar-chart",
            "title": "Top sessions for SQL request: " + kairos["DBORAASHSQLSES"],
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
                                    "query": "DBORAASHSQLSES",
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
