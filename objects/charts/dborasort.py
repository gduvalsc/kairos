class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASORT",
            "icon": "bar-chart",
            "title": "Sorts",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Average number of sorts per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "CC",
                            "datasets": [
                                {
                                    "query": "DBORASORTS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                    ]
                },
                {
                    "title": "Average number of sorted rows per second",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASORTROWS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
