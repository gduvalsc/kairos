class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITR$$2",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'reads' as label , sum(value) as value from (select timestamp, 'xxx'::text as label, reads as value from DBORABUF where bufpool='R') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)