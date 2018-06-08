class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHBFSES$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, session_id||' - '||program as label, kairos_count * 1.0 /ashcoeff() as value from ORAHAS where session_type = 'FOREGROUND' and blocking_session != '') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)