class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACDBCPU",
            "icon": "bar-chart",
            "title": "RAC summary - DB CPU per instance",
            "subtitle": "",
            "collections": ['DBORARACTM'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "DB CPU (sec)",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACDBCPUPI",
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
                                    "query": "DBORARACDBCPU",
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
