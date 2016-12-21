class UserObject(dict):
    def __init__(s):
        if 'EBSPRGQUEW' not in kairos: kairos['EBSPRGQUEW'] = ''
        object = {
            "type": "chart",
            "id": "EBSPRGQUEW",
            "icon": "bar-chart",
            "title": "E-Business Suite - Top waiting queues for program: " + kairos["EBSPRGQUEW"],
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
                                    "query": "EBSTOPPRGQUEW",
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
                                    "query": "EBSALLPRGQUEW",
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
                                    "query": "EBSALLPRGQUEWRT",
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
