class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSESV$$5",
            "collections": [
                "DBORASRV"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'DB Wait time'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, dbtime - cpu as value from DBORASRV where service = '%(DBORASV)s') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)