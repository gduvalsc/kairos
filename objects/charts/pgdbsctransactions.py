class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGDBSCTRANSACTIONS",
            "title": "Database %(PGDBSCTRANSACTIONS)s: Top transactions",
            "subtitle": "",
            "reftime": "PGDBSREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Number of backends",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "PGDBSCTRANSACTIONS$$1",
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
                                    "query": "PGDBSCTRANSACTIONS$$2",
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
