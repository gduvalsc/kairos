class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXACLLOSIODS$$1",
            "collections": [
                "EXATOPCLLOSIOL"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, type || ' - ' || cell as label, stime as value from EXATOPCLLOSIOL where type like 'H/%') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)