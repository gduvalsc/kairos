class UserObject(dict):
    def __init__(s):
        object = {
            "type": "chart",
            "id": "DBORARACDBWAITEI",
            "icon": "bar-chart",
            "title": "Foreground wait events per instance",
            "subtitle": "",
            "collections": ['DBORARACTTFE'],
            "reftime": "DBORARACREFTIME",
            "yaxis": [
                {
                    "title": "# of seconds each second",
                    "scaling": "linear",
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "query": "DBORARACDBWAITEPEI",
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
                                    "query": "DBORARACDBWAITE",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                },
                            ]
                        }
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
