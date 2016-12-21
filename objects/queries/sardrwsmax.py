class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDRWSMAX",
            "collection": "SARD",
            "filterable": False,
            "request": "select timestamp, 'Max throughput (all disks)' label, max(rws) value from SARD group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
