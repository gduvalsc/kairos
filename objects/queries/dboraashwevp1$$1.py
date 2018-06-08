class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHWEVP1$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, p1 as label, kairos_count * 1.0 /ashcoeff() as value from ORAHAS where session_type = 'FOREGROUND' and session_state = 'WAITING' and event = '%(DBORAASHWEVP1)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)