class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORAHFMSI",
            "icon": "bar-chart",
            "title": "Top FMS - Invalidations",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "# of invalidations per second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAHFMSI",
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
                                    "query": "DBORAHFMSIC",
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
