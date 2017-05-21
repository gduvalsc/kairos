class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONTOPMEM",
            "title": "Top processes consuming memory",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Size",
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
                                        "NMONTOP"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select t.timestamp timestamp, t.process||'-'||command label, value from (select timestamp, process, value+0.0 value from NMONTOP where id='ResData') t, (select timestamp, process, value command from NMONTOP where id='Command') s where t.timestamp=s.timestamp and t.process=s.process)",
                                            "projection": "label",
                                            "restriction": "",
                                            "value": "value"
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
                                    "projection": "'All captured processes'",
                                    "collections": [
                                        "NMONTOP"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "NMONTOP",
                                            "projection": "'xxx'",
                                            "restriction": "id = 'ResData'",
                                            "value": "value+0.0"
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