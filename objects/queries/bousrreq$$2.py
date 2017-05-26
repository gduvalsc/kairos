class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOUSRREQ$$2",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, 'All requests' label, sum(value) value from (select timestamp, 'xxx' label, executecount * 1.0 / bocoeff() value from BO where user_name = '%(BOUSRREQ)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)