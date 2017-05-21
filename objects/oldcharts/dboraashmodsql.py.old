class UserObject(dict):
    def __init__(s):
        if 'DBORAASHMODSQL' not in kairos: kairos['DBORAASHMODSQL'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHMODSQL",
            "icon": "bar-chart",
            "title": "Top SQL requests for module: " + kairos["DBORAASHMODSQL"],
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
                                    "query": "DBORAASHMODSQL",
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
