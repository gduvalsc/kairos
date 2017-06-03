class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHOV$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, 'on cpu' label, sum(value) value from (select timestamp, 'xxx' label, kairos_count * 1.0 /ashcoeff() value from ORAHAS where session_state = 'ON CPU') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)