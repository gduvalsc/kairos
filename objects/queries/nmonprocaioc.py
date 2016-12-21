class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONPROCAIOC",
            "collection": "NMONPROCAIO",
            "request": "select timestamp, id label, sum(value) value from NMONPROCAIO where id in ('aiocpu') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
