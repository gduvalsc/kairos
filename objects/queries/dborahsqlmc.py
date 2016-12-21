class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLMC",
            "collection": "ORAHQS",
            "request": "select timestamp, 'Captured SQLs' label, sum(sharable_mem) value from ORAHQS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
