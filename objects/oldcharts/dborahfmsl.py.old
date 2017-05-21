class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAHFMSL",
            "icon": "bar-chart",
            "title": "Top FMS - Loads",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of loads per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAHFMSL",
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
                                    "query": "DBORAHFMSLC",
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
