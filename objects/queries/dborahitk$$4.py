class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITK$$4",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'write complete waits' label, sum(value) value from (select timestamp, 'xxx' label, writecompletewaits value from DBORABUF where bufpool='K') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)