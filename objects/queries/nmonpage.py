class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONPAGE",
            "collection": "NMONPAGE",
            "request": "select timestamp, id label, sum(value) value from NMONPAGE where id in ('pgin', 'pgout', 'pgsin', 'pgsout') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
