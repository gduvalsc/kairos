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
            "request": "select timestamp, 'PGA allocated'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, pga_allocated as value from ORAHAS where session_id||' - '||program = '%(DBORAASHSESPGA)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)