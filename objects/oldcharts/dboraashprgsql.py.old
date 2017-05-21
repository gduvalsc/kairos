class UserObject(dict):
    def __init__(s):
        if 'DBORAASHPRGSQL' not in kairos: kairos['DBORAASHPRGSQL'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHPRGSQL",
            "icon": "bar-chart",
            "title": "Top SQL requests for program: " + kairos["DBORAASHPRGSQL"],
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
                                    "query": "DBORAASHPRGSQL",
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
