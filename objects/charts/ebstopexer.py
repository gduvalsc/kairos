class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "EBSTOPEXER",
            "icon": "bar-chart",
            "title": "E-Business Suite - Top running executions",
            "subtitle": "",
            "reftime": "EBSREFTIME",
            "yaxis": [
                {
                    "title": "Average number of programs per unit of time",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "EBSTOPEXER",
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
