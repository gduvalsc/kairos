class UserObject(dict):
    def __init__(s):
        if 'EBSQUEEXER' not in kairos: kairos['EBSQUEEXER'] = ''
        object = {
            "type": "chart",
            "id": "EBSQUEEXER",
            "icon": "bar-chart",
            "title": "E-Business Suite - Top running executions for queue: " + kairos["EBSQUEEXER"],
            "subtitle": "",
            "reftime": "EBSREFTIME",
            "yaxis": [
                {
                    "title": "Average number of concurrent sessions per unit of time",
                    "scaling": "linear",
                    "properties": { "line": { "stroke": "red" }, "text": { "fill": "red" }},
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "EBSTOPQUEEXER",
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
                                    "query": "EBSALLQUEEXER",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "Estimated response time (in minutes)",
                    "scaling": "linear",
                    "position": "right",
                    "properties": { "line": { "stroke": "blue" }, "text": { "fill": "blue" }},
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "EBSALLQUEEXERRT",
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
