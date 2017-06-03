class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORACHOOSESV",
            "title": "Display service: %(DBORASV)s - Average wait",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of seconds per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'User I/O wait time'",
                                    "collections": [
                                        "DBORASVW"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORASVW",
                                            "projection": "'xxx'",
                                            "restriction": "service = '%(DBORASV)s'",
                                            "value": "uiowaitt"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Administrative wait time'",
                                    "collections": [
                                        "DBORASVW"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORASVW",
                                            "projection": "'xxx'",
                                            "restriction": "service = '%(DBORASV)s'",
                                            "value": "admwaitt"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Concurrency wait time'",
                                    "collections": [
                                        "DBORASVW"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORASVW",
                                            "projection": "'xxx'",
                                            "restriction": "service = '%(DBORASV)s'",
                                            "value": "conwaitt"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Network wait time'",
                                    "collections": [
                                        "DBORASVW"
                                    ],
                                    "userfunctions": [],
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "DBORASVW",
                                            "projection": "'xxx'",
                                            "restriction": "service = '%(DBORASV)s'",
                                            "value": "netwaitt"
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
                                    "projection": "'DB Wait time'",
                                    "collections": [
                                        "DBORASRV"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORASRV",
                                            "projection": "'xxx'",
                                            "restriction": "service = '%(DBORASV)s'",
                                            "value": "dbtime - cpu"
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