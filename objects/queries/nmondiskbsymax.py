class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKBSYMAX",
            "collection": "NMONDISKBUSY",
            "filterable": True,
            "request": "select timestamp, 'Max busy' label, max(value) value from NMONDISKBUSY group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
