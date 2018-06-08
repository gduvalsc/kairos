class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSNETRECVBYTES",
            "title": "Top interfaces - Volume - Received bytes",
            "subtitle": "",
            "reftime": "PGSYSREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Throughput",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "PGSYSNETRECVBYTES$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {
                                        "variable": "PGSYSINTERFACE",
                                        "chart": "PGSYSCHOOSEINTERFACE",
                                        "action": "dispchart"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "PGSYSNETRECVBYTES$$2",
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