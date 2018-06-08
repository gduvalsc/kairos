class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHSQLL",
            "title": "Top SQL - Loads",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of loads per second",
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
                                    "query": "DBORAHSQLL$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "info": {
                                        "query": "DBORAHHELP",
                                        "variable": "DBORAHELP"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHSQLL$$2",
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