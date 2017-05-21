class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSESPGA' not in kairos: kairos['DBORAASHSESPGA'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSESPGA",
            "icon": "bar-chart",
            "title": "PGA allocated for session: " + kairos["DBORAASHSESPGA"],
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "yaxis": [
                {
                    "title": "Size allocated in bytes",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAASHSESPGA",
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
