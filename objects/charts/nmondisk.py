class UserObject(dict):
    def __init__(s):
        if 'NMONDISK' not in kairos: kairos['NMONDISK'] = ''
        object = {
            "type": "chart",
            "id": "NMONDISK",
            "icon": "bar-chart",
            "title": "Activity for disk: " + kairos["NMONDISK"] ,
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "Read / Write (MB/s)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONDISK1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "NMONDISK2",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "Busy rate (%)",
                    "scaling": "linear",
                    "position": "right",
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONDISK3",
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
