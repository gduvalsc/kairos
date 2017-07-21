class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASUM1",
            "title": "DB CPU & Wait - Gets - Reads - Redo",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "black"
                        },
                        "text": {
                            "fill": "black"
                        }
                    },
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORASUM1$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORASUM1$$2",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of logical reads per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "darkgreen"
                        },
                        "text": {
                            "fill": "darkgreen"
                        }
                    },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASUM1$$3",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of physical reads per second",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "red"
                        },
                        "text": {
                            "fill": "red"
                        }
                    },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASUM1$$4",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "# of redo bytes per second",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {
                        "line": {
                            "stroke": "blue"
                        },
                        "text": {
                            "fill": "blue"
                        }
                    },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASUM1$$5",
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