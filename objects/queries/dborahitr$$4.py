class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITR$$4",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'write complete waits' as label, writecompletewaits as value from DBORABUF where bufpool='R') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)