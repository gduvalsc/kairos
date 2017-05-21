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
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sql_plan_operation||' - '||sql_plan_options||' - '||sql_plan_line_id label, kairos_count * 1.0 /ashcoeff() value from ORAHAS where sql_id = '%(DBORAASHSQLEPO)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)