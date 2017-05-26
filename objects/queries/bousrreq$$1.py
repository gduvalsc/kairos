class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOUSRREQ$$1",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, report||' - '||event_id||' (duration: '||duration||')' label, executecount * 1.0 / bocoeff() value from BO where user_name = '%(BOUSRREQ)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)