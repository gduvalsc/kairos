class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONIOADAPTRA",
            "title": "IO Adapters - Read activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Volume (MB/s)",
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
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "NMONIOADAPT"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONIOADAPT",
                                            "projection": "id",
                                            "restriction": "id like '%read%'",
                                            "value": "value / 1024.0"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'All adapters (read)'",
                                    "collections": [
                                        "NMONIOADAPT"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONIOADAPT",
                                            "projection": "'xxx'",
                                            "restriction": "id like '%read%'",
                                            "value": "value / 1024.0"
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