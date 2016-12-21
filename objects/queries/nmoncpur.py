class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPUR",
            "collection": "NMONPROC",
            "request": "select timestamp, id label, sum(value) value from NMONPROC where id in ('Runnable') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
