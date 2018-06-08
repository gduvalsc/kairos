class UserObject(dict):
    def __init__(s):
        object = {
            "id": "TTSQLTOPP",
            "title": "Top SQL by prepares",
            "subtitle": "",
            "reftime": "TTREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of prepares per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "TTSQLTOPP"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "TTSQLTOPP",
                                            "projection": "hashid",
                                            "restriction": "",
                                            "value": "prepares"
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