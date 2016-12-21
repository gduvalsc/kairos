class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVM",
            "collection": "ORAHQS",
            "filterable": True,
            "request": "select timestamp, plan_hash_value label, sum(sharable_mem) value from ORAHQS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
