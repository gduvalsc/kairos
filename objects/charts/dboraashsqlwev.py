class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSQLWEV' not in kairos: kairos['DBORAASHSQLWEV'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSQLWEV",
            "icon": "bar-chart",
            "title": "Top wait events for SQL request: " + kairos["DBORAASHSQLWEV"],
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
                                    "query": "DBORAASHSQLWEV",
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
