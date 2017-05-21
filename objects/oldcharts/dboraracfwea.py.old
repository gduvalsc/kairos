class UserObject(dict):
    def __init__(s):
        if 'DBORARACFWEA' not in kairos: kairos['DBORARACFWEA'] = ''
        object = {
            "type": "chart",
            "id": "DBORARACFWEA",
            "icon": "bar-chart",
            "title": "Display foreground event: " + kairos["DBORARACFWEA"] + " - average per instance",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "Average time (ms)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACFWEAI",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
