class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHWEB$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, event as label, kairos_count * 1.0 /ashcoeff() as value from ORAHAS where session_type = 'BACKGROUND' and session_state = 'WAITING') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)