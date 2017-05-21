class UserObject(dict):
    def __init__(s):
        if 'DBORAASHPRGWEV' not in kairos: kairos['DBORAASHPRGWEV'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHPRGWEV",
            "icon": "bar-chart",
            "title": "Top wait events for program: " + kairos["DBORAASHPRGWEV"],
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
                                    "query": "DBORAASHPRGWEV",
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
