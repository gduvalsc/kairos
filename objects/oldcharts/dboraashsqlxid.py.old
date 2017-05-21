class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSQLXID' not in kairos: kairos['DBORAASHSQLXID'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSQLXID",
            "icon": "bar-chart",
            "title": "Top execute IDs for SQL request: " + kairos["DBORAASHSQLXID"],
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
                                    "query": "DBORAASHSQLXID",
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
