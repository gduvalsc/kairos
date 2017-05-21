class UserObject(dict):
    def __init__(s):
        if 'DBORAASHWEVSQL' not in kairos: kairos['DBORAASHWEVSQL'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHWEVSQL",
            "icon": "bar-chart",
            "title": "Top SQL requests for event: " + kairos["DBORAASHWEVSQL"],
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
                                    "query": "DBORAASHWEVSQL",
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
