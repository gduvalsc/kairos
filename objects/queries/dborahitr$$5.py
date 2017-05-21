class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITR$$5",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'free buffer waits' label, sum(value) value from (select timestamp, 'xxx' label, freewaits value from DBORABUF where bufpool='R') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)