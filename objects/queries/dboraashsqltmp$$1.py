class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSQLTMP$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Temp space allocated'::text as label, temp_space_allocated as value from ORAHAS where sql_id = '%(DBORAASHSQLTMP)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)