class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGONS$$3",
            "collections": [
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'sessions' as label , sum(value) as value from (select timestamp, sessions as label, sessions as value from DBORAMISC) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)