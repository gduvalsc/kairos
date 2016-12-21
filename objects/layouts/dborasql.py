class UserObject(dict):
    def __init__(s):
        object = {
            "type": "layout",
            "id": "DBORASQL",
            "label": "SQL Overview",
            "icon": "bar-chart",
            "rows": [
                {
                    "cols": [
                        {
                            "chart": "DBORASQE"
                        },
                        {
                            "chart": "DBORASQC"
                        },
                    ]
                },
                {
                    "cols": [
                        {
                            "chart": "DBORASQR"
                        },
                        {
                            "chart": "DBORASQG"
                        },
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)
