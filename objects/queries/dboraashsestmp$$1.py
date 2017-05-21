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
            "request": "select timestamp, 'Temp space allocated' label, sum(value) value from (select timestamp, 'xxx' label, temp_space_allocated value from ORAHAS where session_id||' - '||program = '%(DBORAASHSESTMP)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)