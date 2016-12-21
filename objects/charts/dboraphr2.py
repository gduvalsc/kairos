class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAPHR2",
            "icon": "bar-chart",
            "title": "Logical & Physical reads",
            "subtitle": "",
            "yaxis": [
                {
                    "title": "# of units each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "WL",
                            "datasets": [
                                {
                                    "query": "DBORAPHR",
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
