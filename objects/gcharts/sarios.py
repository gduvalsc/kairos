class UserObject(dict):
    def __init__(s):
        object = {
            "id": "SARIOS",
            "title": "I/O activity",
            "subtitle": "",
            "reftime": "SARREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Number of I/O per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "SARB"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "SARB",
                                            "projection": "'lwrite'",
                                            "restriction": "",
                                            "value": "lwrite"
                                        },
                                        {
                                            "table": "SARB",
                                            "projection": "'lread'",
                                            "restriction": "",
                                            "value": "lread"
                                        },
                                        {
                                            "table": "SARB",
                                            "projection": "'pwrite'",
                                            "restriction": "",
                                            "value": "pwrite"
                                        },
                                        {
                                            "table": "SARB",
                                            "projection": "'pread'",
                                            "restriction": "",
                                            "value": "pread"
                                        },
                                        {
                                            "table": "SARB",
                                            "projection": "'bwrite'",
                                            "restriction": "",
                                            "value": "bwrite"
                                        },
                                        {
                                            "table": "SARB",
                                            "projection": "'bread'",
                                            "restriction": "",
                                            "value": "bread"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)