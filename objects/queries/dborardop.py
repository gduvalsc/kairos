class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOP",
            "collection": "DBORAWEB",
            "request": "select timestamp, event label, sum(time) value from DBORAWEB where event in ('log file parallel write', 'LGWR wait on LNS') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
