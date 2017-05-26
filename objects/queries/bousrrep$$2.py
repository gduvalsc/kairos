class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOUSRREP$$2",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, 'All reports' label, sum(value) value from (select timestamp, 'xxx' label, executecount * 1.0 / bocoeff() value from BO where user_name = '%(BOUSRREP)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)