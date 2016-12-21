class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACDBTIMEP",
            "icon": "bar-chart",
            "title": "RAC summary - DB Time per instance",
            "subtitle": "",
            "collections": ['DBORARACTM'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "renderers": [
                        {
                            "type": "P",
                            "datasets": [
                                {
                                    "query": "DBORARACDBTIMEPI",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
