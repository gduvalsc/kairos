class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSQLPHV' not in kairos: kairos['DBORAASHSQLPHV'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSQLPHV",
            "icon": "bar-chart",
            "title": "Top SQL plan hash values for SQL request: " + kairos["DBORAASHSQLPHV"],
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
                                    "query": "DBORAASHSQLPHV",
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
