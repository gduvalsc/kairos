class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORASCAN",
            "icon": "bar-chart",
            "title": "Table scans",
            "subtitle": "",
            "yaxis": [
                {
                    "title": "Average number of table scans per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORASCAN",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
