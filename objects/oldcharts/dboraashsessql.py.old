class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSESSQL' not in kairos: kairos['DBORAASHSESSQL'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSESSQL",
            "icon": "bar-chart",
            "title": "Top SQL requests for session: " + kairos["DBORAASHSESSQL"],
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
                                    "query": "DBORAASHSESSQL",
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
