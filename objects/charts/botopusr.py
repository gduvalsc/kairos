class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "BOTOPUSR",
            "icon": "bar-chart",
            "title": "Business Objects - Top users",
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
                                    "query": "BOTOPUSR",
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
                                    "query": "BOALLUSR",
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
