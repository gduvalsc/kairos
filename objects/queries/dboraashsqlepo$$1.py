class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSQLEPO$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sql_plan_operation||' - '||sql_plan_options||' - '||sql_plan_line_id as label, kairos_count * 1.0 /ashcoeff() as value from ORAHAS where sql_id = '%(DBORAASHSQLEPO)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)