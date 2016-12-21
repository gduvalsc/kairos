class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSM",
            "collection": "ORAHQS",
            "filterable": True,
            "request": "select timestamp, force_matching_signature label, sum(sharable_mem) value from ORAHQS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
