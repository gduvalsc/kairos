class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXACLLOSIOFV$$1",
            "collections": [
                "EXATOPCLLOSIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, type || ' - ' || cell as label, vaverage as value from EXATOPCLLOSIO where type like 'F/%') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)