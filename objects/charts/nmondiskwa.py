class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONDISKWA",
            "title": "Disks - Write activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Volume (MB/s)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "NMONDISKWA$$1",
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
                                    "query": "NMONDISKWA$$2",
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