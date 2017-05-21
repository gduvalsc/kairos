class UserObject(dict):
    def __init__(s):
        if 'DBORAASHPRGSES' not in kairos: kairos['DBORAASHPRGSES'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHPRGSES",
            "icon": "bar-chart",
            "title": "Top sessions for program: " + kairos["DBORAASHPRGSES"],
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
                                    "query": "DBORAASHPRGSES",
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
