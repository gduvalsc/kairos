class UserObject(dict):
    def __init__(s):
        if 'DBORAASHWEVSES' not in kairos: kairos['DBORAASHWEVSES'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHWEVSES",
            "icon": "bar-chart",
            "title": "Top sessions for event: " + kairos["DBORAASHWEVSES"],
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
                                    "query": "DBORAASHWEVSES",
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
