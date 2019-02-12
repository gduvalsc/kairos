class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSESSQL$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sql_id as label, kairos_count * 1.0 /ashcoeff as value from ORAHAS, (select ashcoeff() as ashcoeff) as foo where session_id||' - '||program = '%(DBORAASHSESSQL)s' and sql_id != '') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)