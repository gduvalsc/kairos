class UserObject(dict):
    def __init__(s):
        if 'EBSNODPRGR' not in kairos: kairos['EBSNODPRGR'] = ''
        object = {
            "type": "chart",
            "id": "EBSNODPRGR",
            "icon": "bar-chart",
            "title": "E-Business Suite - Top running programs for node: " + kairos["EBSNODPRGR"],
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
                                    "query": "EBSTOPNODPRGR",
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
                                    "query": "EBSALLNODPRGR",
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
                                    "query": "EBSALLNODPRGRRT",
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
