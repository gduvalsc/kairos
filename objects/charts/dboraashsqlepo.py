class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSQLEPO' not in kairos: kairos['DBORAASHSQLEPO'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSQLEPO",
            "icon": "bar-chart",
            "title": "Top SQL plan operations for SQL request: " + kairos["DBORAASHSQLEPO"],
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
                                    "query": "DBORAASHSQLEPO",
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
