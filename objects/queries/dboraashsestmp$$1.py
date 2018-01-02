class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSESTMP$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, 'Temp space allocated'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, temp_space_allocated as value from ORAHAS where session_id||' - '||program = '%(DBORAASHSESTMP)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)