class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSESWEV' not in kairos: kairos['DBORAASHSESWEV'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSESWEV",
            "icon": "bar-chart",
            "title": "Top wait events for session: " + kairos["DBORAASHSESWEV"],
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
                                    "query": "DBORAASHSESWEV",
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
