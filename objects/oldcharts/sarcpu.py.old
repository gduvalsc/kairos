class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "SARCPU",
            "icon": "bar-chart",
            "title": "CPU Usage - Run / Swap queue",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "collections": ['SARU', 'SARQ'],
            "yaxis": [
                {
                    "title": "CPU Usage (%)",
                    "scaling": "linear",
                    "minvalue": 0,
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "SARCPUSYS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARCPUUSR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        },
                    ]
                },
                {
                    "title": "Run / Swap queue size",
                    "scaling": "linear",
                    "position": "right",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "SARRUNQSZ",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARSWPQSZ",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        }
                    ]
                }
            ],
        }
        super(UserObject, s).__init__(**object)
