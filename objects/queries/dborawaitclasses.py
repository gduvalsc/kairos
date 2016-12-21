class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAWAITCLASSES",
            "collection": "DBORAWEC",
            "filterable": True,
            "request": "select timestamp, eclass label, sum(time) value from DBORAWEC where eclass != 'DB CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
