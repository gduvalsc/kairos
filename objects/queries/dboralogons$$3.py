class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGONS$$3",
            "collections": [
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'sessions' label, sum(value) value from (select timestamp, sessions label, sessions value from DBORAMISC) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)