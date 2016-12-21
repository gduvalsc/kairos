class UserObject(dict):
    def __init__(s):
        if 'BOREPREQ' not in kairos: kairos['BOREPREQ'] = ''
        object = {
            "type": "chart",
            "id": "BOREPREQ",
            "icon": "bar-chart",
            "title": "Business Objects - Top requests for report: " + kairos["BOREPREQ"],
            "subtitle": "",
            "reftime": "BOREFTIME",
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
                                    "query": "BOTOPREPREQ",
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
                                    "query": "BOALLREPREQ",
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
                                    "query": "BOALLREPREQRT",
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
