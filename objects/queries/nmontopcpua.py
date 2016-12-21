class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPCPUA",
            "collection": "NMONTOP",
            "request": "select timestamp, 'All captured processes' label, sum((value+0) / 100.0) value from NMONTOP where id='%CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
