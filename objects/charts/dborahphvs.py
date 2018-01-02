class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHPHVS",
            "title": "Top PHV - Sorts",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of sorts per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORAHPHVS$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "info": {
                                        "query": "DBORAHHELPP",
                                        "variable": "DBORAHELPP"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHPHVS$$2",
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