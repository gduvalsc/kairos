class UserObject(dict):
    def __init__(s):
        if 'DBORAASHMODSES' not in kairos: kairos['DBORAASHMODSES'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHMODSES",
            "icon": "bar-chart",
            "title": "Top sessions for module: " + kairos["DBORAASHMODSES"],
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
                                    "query": "DBORAASHMODSES",
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
