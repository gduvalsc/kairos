class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONMEMOV",
            "title": "Memory overview",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Memory size (MB)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "NMONMEM"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONMEM",
                                            "projection": "id",
                                            "restriction": "id in ('memtotal','swaptotal','memfree','Real free(MB)','Real total(MB)','Virtual free(MB)','Virtual total(MB)')",
                                            "value": "value"
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