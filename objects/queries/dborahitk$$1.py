class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITK$$1",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'gets' as label , sum(value) as value from (select timestamp, 'xxx'::text as label, gets as value from DBORABUF where bufpool='K') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)