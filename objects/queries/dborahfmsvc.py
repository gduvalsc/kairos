class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSVC",
            "collection": "ORAHQS",
            "request": "select timestamp, 'Captured FMSs' label, sum(version_count) value from ORAHQS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
