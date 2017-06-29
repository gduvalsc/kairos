class UserObject(dict):
    def __init__(s):
        object = {
            "type": "menu",
            "id": "POSTGRES",
            "tablecondition": "vkpg_stat_database",
            "icon": "fa fa-database",
            "label": "PostgreSQL Database",
            "items" : [
                {
                    "type": "submenu",
                    "label": "Database Metrics ",
                    "items": [
                        {
                            "type": "submenu",
                            "label": "Overview",
                            "items": [
                                { "type": "menuitem", "label": "Backends per database", "action": "dispchart", "chart": "PGDBOVBACKENDS"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Databases read times", "action": "dispchart", "chart": "PGDBOVREADT"},
                                { "type": "menuitem", "label": "Databases write times", "action": "dispchart", "chart": "PGDBOVWRITET"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Read blocks per database", "action": "dispchart", "chart": "PGDBOVREADB"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Inserted rows", "action": "dispchart", "chart": "PGDBOVINSERTS"},
                                { "type": "menuitem", "label": "Updated rows", "action": "dispchart", "chart": "PGDBOVUPDATES"},
                                { "type": "menuitem", "label": "Deleted rows", "action": "dispchart", "chart": "PGDBOVDELETES"},
                                { "type": "menuitem", "label": "Fetched rows", "action": "dispchart", "chart": "PGDBOVFETCHES"},
                                { "type": "menuitem", "label": "Returned rows", "action": "dispchart", "chart": "PGDBOVSELECTS"},
                                { "type": "menuitem", "label": "Commits", "action": "dispchart", "chart": "PGDBOVCOMMITS"},
                                { "type": "menuitem", "label": "Rollbacks", "action": "dispchart", "chart": "PGDBOVROLLBACKS"},
                            ]
                        },
                    ]
                },
                { "type": "separator", "tablecondition": "vpsutil_cpu_times"},
                {
                    "type": "submenu",
                    "tablecondition": "vpsutil_cpu_times",
                    "label": "System metrics",
                    "items": [
                        { "type": "menuitem", "label": "CPU usage", "action": "dispchart", "chart": "PGSYSCPU"},
                        { "type": "separator", "tablecondition": "vpsutil_swap_memory"},
                        { "type": "menuitem", "tablecondition": "vpsutil_swap_memory", "label": "Swapping activity", "action": "dispchart", "chart": "PGSYSSWP"},
                        { "type": "separator", "tablecondition": "vpsutil_virtual_memory"},
                        { "type": "menuitem", "tablecondition": "vpsutil_virtual_memory", "label": "Memory usage", "action": "dispchart", "chart": "PGSYSMEM"},
                        { "type": "separator", "tablecondition": "vpsutil_disk_io_counters"},
                        {
                            "type": "submenu",
                            "tablecondition": "vpsutil_disk_io_counters",
                            "label": "Disks activity",
                            "items": [
                                { "type": "menuitem", "label": "Top disks (read volume)", "action": "dispchart", "chart": "PGSYSDSKREADBYTES"},
                                { "type": "menuitem", "label": "Top disks (write volume)", "action": "dispchart", "chart": "PGSYSDSKWRITEBYTES"},
                                { "type": "menuitem", "label": "Top disks (read count)", "action": "dispchart", "chart": "PGSYSDSKREADCOUNT"},
                                { "type": "menuitem", "label": "Top disks (write count)", "action": "dispchart", "chart": "PGSYSDSKWRITECOUNT"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Choose disk...", "action": "dispchoice", "choice": "PGSYSDISK"},
                            ]
                        },
                        { "type": "separator", "tablecondition": "vpsutil_net_io_counters"},
                        {
                            "type": "submenu",
                            "tablecondition": "vpsutil_net_io_counters",
                            "label": "Network activity",
                            "items": [
                                { "type": "menuitem", "label": "Top interfaces (received volume)", "action": "dispchart", "chart": "PGSYSNETRECVBYTES"},
                                { "type": "menuitem", "label": "Top interfaces (sent volume)", "action": "dispchart", "chart": "PGSYSNETSENTBYTES"},
                                { "type": "menuitem", "label": "Top interfaces (packets sent)", "action": "dispchart", "chart": "PGSYSNETSENTPACKETS"},
                                { "type": "menuitem", "label": "Top interfaces (packets received)", "action": "dispchart", "chart": "PGSYSNETRECVPACKETS"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Choose interface...", "action": "dispchoice", "choice": "PGSYSINTERFACE"},
                            ]
                        },
                        { "type": "separator", "tablecondition": "vpsutil_processes"},
                        {
                            "type": "submenu",
                            "tablecondition": "vpsutil_processes",
                            "label": "Processes",
                            "items": [
                                { "type": "menuitem", "label": "Top processes (CPU time)", "action": "dispchart", "chart": "PGSYSPSCPU"},
                                { "type": "menuitem", "label": "Top process families (CPU time)", "action": "dispchart", "chart": "PGSYSPSCPUF"},
                                { "type": "menuitem", "label": "Top commands (CPU time)", "action": "dispchart", "chart": "PGSYSPSCPUC"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Top processes (Resident memory size)", "action": "dispchart", "chart": "PGSYSPSMEMRSS"},
                                { "type": "menuitem", "label": "Top process families (Resident memory size)", "action": "dispchart", "chart": "PGSYSPSMEMRSSF"},
                                { "type": "menuitem", "label": "Top commands (Resident memory size)", "action": "dispchart", "chart": "PGSYSPSMEMRSSC"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Top processes (Virtual memory size)", "action": "dispchart", "chart": "PGSYSPSMEMVMS"},
                                { "type": "menuitem", "label": "Top process families (Virtual memory size)", "action": "dispchart", "chart": "PGSYSPSMEMVMSF"},
                                { "type": "menuitem", "label": "Top commands (Virtual memory size)", "action": "dispchart", "chart": "PGSYSPSMEMVMSC"},
                                { "type": "separator"},
                                { "type": "menuitem", "label": "Choose process...", "action": "dispchoice", "choice": "PGSYSPROCESS"},
                                { "type": "menuitem", "label": "Choose family...", "action": "dispchoice", "choice": "PGSYSFAMILY"},
                                { "type": "menuitem", "label": "Choose command...", "action": "dispchoice", "choice": "PGSYSCOMMAND"},
                            ]
                        },
                    ]
                },
            ]
        }
        super(UserObject, s).__init__(**object)
