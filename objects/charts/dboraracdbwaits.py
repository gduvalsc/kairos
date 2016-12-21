class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACDBWAITS",
            "icon": "bar-chart",
            "title": "RAC summary - DB waits per instance",
            "subtitle": "",
            "collections": ['DBORARACTM'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "DB Waits (sec)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACDBWAITSPI",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORARACDBWAITS",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
