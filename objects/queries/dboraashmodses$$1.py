class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHMODSES$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, session_id||' - '||program label, kairos_count * 1.0 /ashcoeff() value from ORAHAS where module = '%(DBORAASHMODSES)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)