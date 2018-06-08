class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGDBOVINSERTS",
            "title": "Overview  - Inserted rows per database",
            "subtitle": "",
            "reftime": "PGDBREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of inserted rows per second",
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
                                    "query": "PGDBOVINSERTS$$1",
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
                                    "query": "PGDBOVINSERTS$$2",
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