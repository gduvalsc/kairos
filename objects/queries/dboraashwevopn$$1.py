class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHWEVOPN$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sql_opname label, kairos_count * 1.0 /ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' and session_state = 'WAITING' and event = '%(DBORAASHWEVOPN)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)