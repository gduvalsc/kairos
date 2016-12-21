class UserObject(dict):
    def __init__(s):
        if 'TTSQLE' not in kairos: kairos['TTSQLE'] = ''
        object = {
            "type": "chart",
            "id": "TTSQLE",
            "icon": "bar-chart",
            "title": "Display SQL: " + kairos["TTSQLE"] + ", execution time / exec",
            "subtitle": "",
            "reftime": "TTREFTIME2",
            "yaxis": [
                {
                    "title": "Execution time per exec (in micro sec)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "TTSQLE",
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
