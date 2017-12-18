class UserObject(dict):
    def __init__(s):
        object = {
            "type": "menu",
            "id": "EXACELL",
            "tablecondition": "EXACPU",
            "icon": "fa fa-desktop",
            "label": "Exadata Cells",
            "items" : [
                {
                    "type": "submenu",
                    "label": "Top cells ...",
                    "items": [
                        { "type": "menuitem", "label": "CPU usage", "action": "dispchart", "chart": "EXACPU" },
                        { "type": "separator"},
                        { "type": "menuitem", "label": "Flash OS IO requests / seconde", "action": "dispchart", "chart": "EXACLLOSIOFR" },
                        { "type": "menuitem", "label": "Flash OS IO megabytes / seconde", "action": "dispchart", "chart": "EXACLLOSIOFV" },
                        { "type": "menuitem", "label": "Flash utilization (%)", "action": "dispchart", "chart": "EXACLLOSIOFU" },
                        { "type": "menuitem", "label": "Flash service time", "action": "dispchart", "chart": "EXACLLOSIOFS" },
                        { "type": "menuitem", "label": "Flash wait time", "action": "dispchart", "chart": "EXACLLOSIOFW" },
                        { "type": "separator"},
                        { "type": "menuitem", "label": "Hard disk OS IO requests / seconde", "action": "dispchart", "chart": "EXACLLOSIODR" },
                        { "type": "menuitem", "label": "Hard disk OS IO megabytes / seconde", "action": "dispchart", "chart": "EXACLLOSIODV" },
                        { "type": "menuitem", "label": "Hard disk utilization (%)", "action": "dispchart", "chart": "EXACLLOSIODU" },
                        { "type": "menuitem", "label": "Hard disk service time", "action": "dispchart", "chart": "EXACLLOSIODS" },
                        { "type": "menuitem", "label": "Hard disk wait time", "action": "dispchart", "chart": "EXACLLOSIODW" },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Top databases ...",
                    "items": [
                        { "type": "menuitem", "label": "IO requests on flash / second", "action": "dispchart", "chart": "EXADBIOFR" },
                        { "type": "menuitem", "label": "IO requests on disk / second", "action": "dispchart", "chart": "EXADBIODR" },
                        { "type": "separator"},
                        { "type": "menuitem", "label": "IO throughput on flash / second", "action": "dispchart", "chart": "EXADBIOFV" },
                        { "type": "menuitem", "label": "IO throughput on disk / second", "action": "dispchart", "chart": "EXADBIODV" },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Top hard disks ...",
                    "items": [
                        { "type": "menuitem", "label": "Hard disk OS IO requests / seconde", "action": "dispchart", "chart": "EXADSKOSIODR" },
                        { "type": "menuitem", "label": "Hard disk OS IO megabytes / seconde", "action": "dispchart", "chart": "EXADSKOSIODV" },
                        { "type": "menuitem", "label": "Hard disk utilization (%)", "action": "dispchart", "chart": "EXADSKOSIODU" },
                        { "type": "menuitem", "label": "Hard disk service time", "action": "dispchart", "chart": "EXADSKOSIODS" },
                        { "type": "menuitem", "label": "Hard disk wait time", "action": "dispchart", "chart": "EXADSKOSIODW" },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Top flash devices ...",
                    "items": [
                        { "type": "menuitem", "label": "Flash OS IO requests / seconde", "action": "dispchart", "chart": "EXADSKOSIOFR" },
                        { "type": "menuitem", "label": "Flash OS IO megabytes / seconde", "action": "dispchart", "chart": "EXADSKOSIOFV" },
                        { "type": "menuitem", "label": "Flash utilization (%)", "action": "dispchart", "chart": "EXADSKOSIOFU" },
                        { "type": "menuitem", "label": "Flash service time", "action": "dispchart", "chart": "EXADSKOSIOFS" },
                        { "type": "menuitem", "label": "Flash wait time", "action": "dispchart", "chart": "EXADSKOSIOFW" },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
