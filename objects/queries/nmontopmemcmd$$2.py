class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPMEMCMD$$2",
            "collections": [
                "NMONTOP"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'All captured commands' label, sum(value) value from (select timestamp, 'xxx' label, value+0.0 value from NMONTOP where id = 'ResData') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)