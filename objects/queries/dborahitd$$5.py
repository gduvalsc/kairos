class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITD$$5",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'free buffer waits' as label, freewaits as value from DBORABUF where bufpool='D') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)