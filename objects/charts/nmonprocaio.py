class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "NMONPROCAIO",
            "icon": "bar-chart",
            "title": "Asynchronous I/O activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "yaxis": [
                {
                    "title": "# of aio processors /running aios",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONPROCAIO",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                           ]
                        }
                    ]
                },
                {
                    "title": "CPU used by asynchronous I/O (%) of aio processors /running aios",
                    "scaling": "linear",
                    "maxvalue": 110,
                    "minvalue": 0,
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "NMONPROCAIOC",
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
