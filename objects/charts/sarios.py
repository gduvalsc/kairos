class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "SARIOS",
            "icon": "bar-chart",
            "title": "I/O activity",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "collections": ['SARB'],
            "yaxis": [
                {
                    "title": "Number of I/O per second",
                    "scaling": "linear",
                    "minvalue": 0,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "SARIOSLW",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARIOSLR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARIOSPW",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARIOSPR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARIOSBW",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "SARIOSBR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                           ]
                        },
                    ]
                },
            ],
        }
        super(UserObject, s).__init__(**object)
