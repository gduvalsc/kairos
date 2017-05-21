class UserObject(dict):
    def __init__(s):
        if 'DBORAASHMODWEV' not in kairos: kairos['DBORAASHMODWEV'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHMODWEV",
            "icon": "bar-chart",
            "title": "Top wait events for module: " + kairos["DBORAASHMODWEV"],
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
                                    "query": "DBORAASHMODWEV",
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
