class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAASHMODSQL",
            "title": "Top SQL requests for module: %(DBORAASHMODSQL)s",
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "Number of active sessions",
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
                                    "query": "DBORAASHMODSQL$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value",
                                    "info": {
                                        "variable": "DBORAHELP",
                                        "query": "DBORAHHELP"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)