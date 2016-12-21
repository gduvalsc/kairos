class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDSVCMAX",
            "collection": "SARD",
            "filterable": False,
            "request": "select timestamp, 'Max service time (all disks)' label, max(avserv) value from SARD group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
