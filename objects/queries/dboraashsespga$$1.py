class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSESPGA$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, 'PGA allocated' label, sum(value) value from (select timestamp, 'xxx' label, pga_allocated value from ORAHAS where session_id||' - '||program = '%(DBORAASHSESPGA)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)