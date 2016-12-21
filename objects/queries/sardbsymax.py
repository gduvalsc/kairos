class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDBSYMAX",
            "collection": "SARD",
            "filterable": False,
            "request": "select timestamp, 'Max (%) all disks' label, max(busy) value from SARD group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
