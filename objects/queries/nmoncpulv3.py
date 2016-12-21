class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPULV3",
            "collection": "NMONCPU",
            "request": "select timestamp, 'Logical CPU (computation 1) %' label, avg(user + sys) value from NMONCPU where id='ALL' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
