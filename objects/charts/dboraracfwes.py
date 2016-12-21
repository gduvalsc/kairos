class UserObject(dict):
    def __init__(s):
        if 'DBORARACFWES' not in kairos: kairos['DBORARACFWES'] = ''
        object = {
            "type": "chart",
            "id": "DBORARACFWES",
            "icon": "bar-chart",
            "title": "Display foreground event: " + kairos["DBORARACFWES"] + " - sum per instance",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "# of seconds per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACFWESI",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACFWES",
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
