null=None
true=True
false=False

class UserObject(dict):
    def __init__(self):
        object = {
            "id": "DBORARACDBWAITEI",
            "title": "Foreground wait events per instance",
            "subtitle": "",
            "reftime": "DBORARACREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "gray"
                        },
                        "text": {
                            "fill": "gray"
                        }
                    },
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACDBWAITEI$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACDBWAITEI$$2",
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
        super(UserObject, self).__init__(**object)
