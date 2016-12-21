class UserObject(dict):
    def __init__(s):
        object = {
            "type": "menu",
            "id": "TT",
            "tablecondition": "TTMISC",
            "icon": "database",
            "label": "Oracle Timesten",
            "menuwidth": 150,
            "itemswidth": 200,
            "items" : [
                {
                    "type": "submenu",
                    "itemswidth": 300,
                    "label": "SQL Statistics",
                    "items": [
                        { "type": "menuitem", "label": "Top SQL by executions", "action": "dispchart", "chart": "TTSQLTOPX" },
                        { "type": "menuitem", "label": "Top SQL by preparations", "action": "dispchart", "chart": "TTSQLTOPP" },
                        { "type": "separator"},
                        { "type": "menuitem", "label": "Top SQL by execution time", "action": "dispchart", "chart": "TTSQLTOPXT" },
                        { "type": "separator"},
                        { "type": "menuitem", "label": "Choose SQL, statistics per second", "action": "dispchoice", "choice": "TTSQLT" },
                        { "type": "menuitem", "label": "Choose SQL, statistics per execution", "action": "dispchoice", "choice": "TTSQLE" },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "itemswidth": 300,
                    "label": "Statistics",
                    "items": [
                        { "type": "menuitem", "label": "Stmt statistics", "action": "dispchart", "chart": "TTSTMTSTATS" },
                        { "type": "menuitem", "label": "Txn statistics", "action": "dispchart", "chart": "TTTXNSTATS" },
                        { "type": "menuitem", "label": "DB Table statistics", "action": "dispchart", "chart": "TTDBTABLESTATS" },
                        { "type": "menuitem", "label": "DB Index statistics", "action": "dispchart", "chart": "TTDBINDEXSTATS" },
                        { "type": "separator"},
                        { "type": "menuitem", "label": "Choose statistic", "action": "dispchoice", "choice": "TTSTA" },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
