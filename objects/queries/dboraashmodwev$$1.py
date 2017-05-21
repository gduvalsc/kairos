class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHMODWEV$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, case when event = '' then 'on cpu' when event != '' then event end label, kairos_count * 1.0 /ashcoeff() value from ORAHAS where module = '%(DBORAASHMODWEV)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)