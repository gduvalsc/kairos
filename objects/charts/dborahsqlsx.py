class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHSQLSX",
            "title": "SQL request: %(DBORAHSQLSX)s - Statistics per execution",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Elapsed (sec) per execution",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHSQLSX$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Buffer gets & disk reads per exec",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHSQLSX$$2",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHSQLSX$$3",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Executions and fetches per exec",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHSQLSX$$4",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHSQLSX$$5",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Rows processed per exec",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHSQLSX$$6",
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