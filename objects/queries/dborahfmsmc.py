class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSMC",
            "collection": "ORAHQS",
            "request": "select timestamp, 'Captured FMSs' label, sum(sharable_mem) value from ORAHQS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
