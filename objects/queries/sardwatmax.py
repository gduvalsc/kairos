class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDWATMAX",
            "collection": "SARD",
            "filterable": False,
            "request": "select timestamp, 'Max wait time (all disks)' label, max(avwait) value from SARD group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
