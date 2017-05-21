class UserObject(dict):
    def __init__(s):
        if 'DBORAHFMSTX' not in kairos: kairos['DBORAHFMSTX'] = ''
        object = {
            "type": "chart",
            "id": "DBORAHFMSTX",
            "icon": "bar-chart",
            "title": "FMS: " + kairos["DBORAHFMSTX"] + " - Statistics per execution",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Elapsed (sec) per execution",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORAHFMSTXWA",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHFMSTXWC",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHFMSTXWI",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHFMSTXWR",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                                {
                                    "query": "DBORAHFMSTXC",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORAHFMSTXE",
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
