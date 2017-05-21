class UserObject(dict):
    def __init__(s):
        if 'DBORATBS' not in kairos: kairos['DBORATBS'] = ''
        object = {
            "type": "chart",
            "id": "DBORACHOOSETBS",
            "icon": "bar-chart",
            "title": "Display average time for tablespace: " + kairos["DBORATBS"],
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "yaxis": [
                {
                    "title": "Average time per operation (ms)",
                    "scaling": "linear",
                    "properties": { "line": { "stroke": "red" }, "text": { "fill": "red" } },
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACHOOSETBSAVG",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "Number of reads per seconds",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACHOOSETBSNUM",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
                {
                    "title": "Number of blocks per read",
                    "scaling": "linear",
                    "position": "right",
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORACHOOSETBSBLKR",
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
