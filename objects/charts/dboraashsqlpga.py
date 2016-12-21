class UserObject(dict):
    def __init__(s):
        if 'DBORAASHSQLPGA' not in kairos: kairos['DBORAASHSQLPGA'] = ''
        object = {
            "type": "chart",
            "id": "DBORAASHSQLPGA",
            "icon": "bar-chart",
            "title": "PGA allocated for SQL request: " + kairos["DBORAASHSQLPGA"],
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "yaxis": [
                {
                    "title": "Size allocated in bytes",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAASHSQLPGA",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
