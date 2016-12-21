class UserObject(dict):
    def __init__(s):
        object = {
            "type": "menu",
            "id": "SAR",
            "tablecondition": "SARU",
            "icon": "desktop",
            "label": "SAR",
            "menuwidth": 80,
            "itemswidth": 200,
            "items" : [
                { "type": "menuitem", "label": "CPU usage - Run queue", "action": "dispchart", "chart": "SARCPU" },
                { "type": "separator"},
                { "type": "menuitem", "label": "IO activity", "action": "dispchart", "chart": "SARIOS" },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "itemswidth": 200,
                    "label": "Disks",
                    "items": [
                        { "type": "menuitem", "label": "Disks - Saturation", "action": "dispchart", "chart": "SARDBSY" },
                        { "type": "menuitem", "label": "Disks - Throughput", "action": "dispchart", "chart": "SARDRWS" },
                        { "type": "menuitem", "label": "Disks - Service time", "action": "dispchart", "chart": "SARDSVC" },
                        { "type": "menuitem", "label": "Disks - Wait time", "action": "dispchart", "chart": "SARDWAT" },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
