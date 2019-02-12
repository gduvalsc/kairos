class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHPRGWEV$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, case when event is null then 'on cpu' when event is not null then event end as label, kairos_count * 1.0 /ashcoeff as value from ORAHAS, (select ashcoeff() as ashcoeff) as foo where program = '%(DBORAASHPRGWEV)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)