class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSQLWEV$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, case when event = '' then 'on cpu' when event != '' then event end as label, kairos_count * 1.0 /ashcoeff() as value from ORAHAS where sql_id = '%(DBORAASHSQLWEV)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)