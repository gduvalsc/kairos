class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHTXOPN$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sql_opname as label, kairos_count * 1.0 /ashcoeff() as value from ORAHAS where xid = '%(DBORAASHTXOPN)s' and sql_opname != '') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)