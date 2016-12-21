class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSV",
            "collection": "ORAHQS",
            "filterable": True,
            "request": "select timestamp, force_matching_signature label, sum(version_count) value from ORAHQS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
