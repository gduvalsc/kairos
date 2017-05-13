class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASYS",
            "title": "System statistics",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chartj",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAOSS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select t.timestamp, statistic, value, avgelapsed from (select *, 'abcdef' kairosnode from DBORAOSS) t, (select *, 'abcdef' kairosnode from DBORAMISC) m where t.timestamp=m.timestamp and t.kairosnode=m.kairosnode)",
                                            "projection": "statistic",
                                            "restriction": "statistic in ('USER_TIME','SYS_TIME')",
                                            "value": "value*1.0/100/avgelapsed"
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
                                    "projection": "label",
                                    "collections": [
                                        "DBORAOSS"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "DBORAOSS",
                                            "projection": "statistic",
                                            "restriction": "statistic='NUM_CPUS'",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Run Queue / Load",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {
                        "text": {
                            "fill": "blue"
                        },
                        "line": {
                            "stroke": "blue"
                        }
                    },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAOSS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select t.timestamp, statistic, value, avgelapsed from (select *, 'abcdef' kairosnode from DBORAOSS) t, (select *, 'abcdef' kairosnode from DBORAMISC) m where t.timestamp=m.timestamp and t.kairosnode=m.kairosnode)",
                                            "projection": "statistic",
                                            "restriction": "statistic in ('OS_CPU_WAIT_TIME')",
                                            "value": "value*1.0/100/avgelapsed"
                                        },
                                        {
                                            "table": "(select t.timestamp, statistic, value, avgelapsed from (select *, 'abcdef' kairosnode from DBORAOSS) t, (select *, 'abcdef' kairosnode from DBORAMISC) m where t.timestamp=m.timestamp and t.kairosnode=m.kairosnode)",
                                            "projection": "statistic",
                                            "restriction": "statistic in ('LOAD')",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "IO wait time",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {
                        "text": {
                            "fill": "green"
                        },
                        "line": {
                            "stroke": "green"
                        }
                    },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "DBORAOSS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select t.timestamp, statistic, value, avgelapsed from (select *, 'abcdef' kairosnode from DBORAOSS) t, (select *, 'abcdef' kairosnode from DBORAMISC) m where t.timestamp=m.timestamp and t.kairosnode=m.kairosnode)",
                                            "projection": "statistic",
                                            "restriction": "statistic in ('IOWAIT_TIME')",
                                            "value": "value*1.0/100/avgelapsed"
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