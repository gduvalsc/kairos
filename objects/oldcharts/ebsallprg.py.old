class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "EBSALLPRG",
            "icon": "bar-chart",
            "title": "E-Business Suite - Running & Waiting programs",
            "subtitle": "",
            "reftime": "EBSREFTIME",
            "yaxis": [
                {
                    "title": "Average number of programs per unit of time",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "EBSALLPRGR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "EBSALLPRGW",
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
