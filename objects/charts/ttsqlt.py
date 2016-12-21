class UserObject(dict):
    def __init__(s):
        if 'TTSQLT' not in kairos: kairos['TTSQLT'] = ''
        object = {
            "type": "chart",
            "id": "TTSQLT",
            "icon": "bar-chart",
            "title": "Display SQL: " + kairos["TTSQLT"] + ", execution time / sec",
            "subtitle": "",
            "reftime": "TTREFTIME2",
            "yaxis": [
                {
                    "title": "Execution time per second (in ms)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "TTSQLT",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "Number of executions / second",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "TTSQLTN",
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
