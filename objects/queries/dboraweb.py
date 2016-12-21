class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAWEB",
            "collection": "DBORAWEB",
            "filterable": True,
            "userfunctions": ['idlewev', 'pxwev'],
            "request": "select timestamp, event label, sum(time) value from DBORAWEB where not idlewev(event) and not pxwev(event) group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
