class UserObject(dict):
    def __init__(s):
        object = {
            "type": "menu",
            "id": "DASH",
            "tablecondition": "ORAHAS",
            "icon": "database",
            "label": "ASH",
            "items" : [
                {
                    "type": "submenu",
                    "label": "DB Time overview",
                    "items": [
                        { "type": "menuitem", "label": "DB Time", "action": "dispchart", "chart": "DBORAASHDBTIME" },
                        { "type": "menuitem", "label": "Background DB Time", "action": "dispchart", "chart": "DBORAASHBDBTIME" },
                        { "type": "menuitem", "label": "Foreground & Background DB Time", "action": "dispchart", "chart": "DBORAASHOV" },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Wait events",
                    "items": [
                        { "type": "menuitem", "label": " Top foreground wait classes", "action": "dispchart", "chart": "DBORAASHWEC" },
                        { "type": "menuitem", "label": " Top foreground wait events", "action": "dispchart", "chart": "DBORAASHWEV" },
                        { "type": "menuitem", "label": " Top background wait events", "action": "dispchart", "chart": "DBORAASHWEB" },
                        { "type": "separator"},
                        { "type": "submenu", "label": " Choose event ...",
                            "items": [
                                { "type": "menuitem", "label": " Top sessions", "action": "dispchoice", "choice": "DBORAASHWEVSES" },
                                { "type": "menuitem", "label": " Top SQL requests", "action": "dispchoice", "choice": "DBORAASHWEVSQL" },
                                { "type": "menuitem", "label": " Top SQL operations", "action": "dispchoice", "choice": "DBORAASHWEVOPN" },
                            ]
                        },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Sessions",
                    "items": [
                        { "type": "menuitem", "label": " Top foreground sessions", "action": "dispchart", "chart": "DBORAASHSES" },
                        { "type": "menuitem", "label": " Top blocked foreground sessions", "action": "dispchart", "chart": "DBORAASHBFSES" },
                        { "type": "menuitem", "label": " Top blocking sessions", "action": "dispchart", "chart": "DBORAASHHSES" },
                        { "type": "menuitem", "label": " Top background sessions", "action": "dispchart", "chart": "DBORAASHBSES" },
                        { "type": "menuitem", "label": " PGA allocated - Top sessions", "action": "dispchart", "chart": "DBORAASHPGA" },
                        { "type": "menuitem", "label": " Temp space allocated - Top sessions", "action": "dispchart", "chart": "DBORAASHTMP" },
                        { "type": "separator"},
                        { "type": "submenu", "label": " Choose session ...",
                            "items": [
                                { "type": "menuitem", "label": " Top wait events", "action": "dispchoice", "choice": "DBORAASHSESWEV" },
                                { "type": "menuitem", "label": " Top SQL requests", "action": "dispchoice", "choice": "DBORAASHSESSQL" },
                                { "type": "menuitem", "label": " Top SQL operations", "action": "dispchoice", "choice": "DBORAASHSESOPN" },
                                { "type": "menuitem", "label": " PGA allocated", "action": "dispchoice", "choice": "DBORAASHSESPGA" },
                                { "type": "menuitem", "label": " Temp space allocated", "action": "dispchoice", "choice": "DBORAASHSESTMP" },
                            ]
                        },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "SQL requests",
                    "items": [
                        { "type": "menuitem", "label": " Top SQL requests", "action": "dispchart", "chart": "DBORAASHSQL" },
                        { "type": "menuitem", "label": " Top SQL requests on CPU", "action": "dispchart", "chart": "DBORAASHSQLCPU" },
                        { "type": "menuitem", "label": " Top waiting SQL requests", "action": "dispchart", "chart": "DBORAASHSQLWAIT" },
                        { "type": "menuitem", "label": " Top SQL operations", "action": "dispchart", "chart": "DBORAASHOPN" },
                        { "type": "menuitem", "label": " PGA allocated - Top SQL requests", "action": "dispchart", "chart": "DBORAASHPGA2" },
                        { "type": "menuitem", "label": " Temp space allocated - Top SQL requests", "action": "dispchart", "chart": "DBORAASHTMP2" },
                        { "type": "separator"},
                        { "type": "submenu", "label": " Choose SQL request ...",
                            "items": [
                                { "type": "menuitem", "label": " Top wait events", "action": "dispchoice", "choice": "DBORAASHSQLWEV" },
                                { "type": "menuitem", "label": " Top sessions", "action": "dispchoice", "choice": "DBORAASHSQLSES" },
                                { "type": "menuitem", "label": " Top sql plan hash values", "action": "dispchoice", "choice": "DBORAASHSQLPHV" },
                                { "type": "menuitem", "label": " Top execution plan operations", "action": "dispchoice", "choice": "DBORAASHSQLEPO" },
                                { "type": "menuitem", "label": " Top execute IDs", "action": "dispchoice", "choice": "DBORAASHSQLXID" },
                                { "type": "menuitem", "label": " PGA allocated", "action": "dispchoice", "choice": "DBORAASHSQLPGA" },
                                { "type": "menuitem", "label": " Temp space allocated", "action": "dispchoice", "choice": "DBORAASHSQLTMP" },
                            ]
                        },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Modules",
                    "items": [
                        { "type": "menuitem", "label": " Top modules", "action": "dispchart", "chart": "DBORAASHMOD" },
                        { "type": "separator"},
                        { "type": "submenu", "label": " Choose module ...",
                            "items": [
                                { "type": "menuitem", "label": " Top wait events", "action": "dispchoice", "choice": "DBORAASHMODWEV" },
                                { "type": "menuitem", "label": " Top sessions", "action": "dispchoice", "choice": "DBORAASHMODSES" },
                                { "type": "menuitem", "label": " Top SQL requests", "action": "dispchoice", "choice": "DBORAASHMODSQL" },
                            ]
                        },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Programs",
                    "items": [
                        { "type": "menuitem", "label": " Top programs", "action": "dispchart", "chart": "DBORAASHPRG" },
                        { "type": "separator"},
                        { "type": "submenu", "label": " Choose program ...",
                            "items": [
                                { "type": "menuitem", "label": " Top wait events", "action": "dispchoice", "choice": "DBORAASHPRGWEV" },
                                { "type": "menuitem", "label": " Top sessions", "action": "dispchoice", "choice": "DBORAASHPRGSES" },
                                { "type": "menuitem", "label": " Top SQL requests", "action": "dispchoice", "choice": "DBORAASHPRGSQL" },
                            ]
                        },
                    ]
                },
                { "type": "separator"},
                {
                    "type": "submenu",
                    "label": "Machines",
                    "items": [
                        { "type": "menuitem", "label": " Top machines", "action": "dispchart", "chart": "DBORAASHMAC" },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
