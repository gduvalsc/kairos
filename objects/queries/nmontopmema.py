class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPMEMA",
            "collection": "NMONTOP",
            "request": "select timestamp, 'All captured processes' label, sum(value+0.0) value from NMONTOP where id='ResData' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
