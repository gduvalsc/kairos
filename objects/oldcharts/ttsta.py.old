class UserObject(dict):
    def __init__(s):
        if 'TTSTA' not in kairos: kairos['TTSTA'] = ''
        object = {
            "type": "chart",
            "id": "TTSTA",
            "icon": "bar-chart",
            "title": "Display statistic: " + kairos["TTSTA"],
            "subtitle": "",
            "reftime": "TTREFTIME",
            "yaxis": [
                {
                    "title": "# of units each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "TTSTA",
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
