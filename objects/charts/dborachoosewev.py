class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORACHOOSEWEV",
            "title": "Display foreground event: %(DBORAWEV)s",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Average time per operation (ms)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "red"
                        },
                        "text": {
                            "fill": "red"
                        }
                    },
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACHOOSEWEV$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {}
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Number of operations - Timeouts per sec",
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
                                    "query": "DBORACHOOSEWEV$$2",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {}
                                },
                                {
                                    "query": "DBORACHOOSEWEV$$3",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "onclick": {}
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)