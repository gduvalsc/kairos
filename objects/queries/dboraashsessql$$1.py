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
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sql_id label, kairos_count * 1.0 /ashcoeff() value from ORAHAS where session_id||' - '||program = '%(DBORAASHSESSQL)s' and sql_id != '') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)