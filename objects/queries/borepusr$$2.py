class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOREPUSR$$2",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, 'All users' label, sum(value) value from (select timestamp, 'xxx' label, executecount * 1.0 / bocoeff() value from BO where report = '%(BOREPUSR)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)