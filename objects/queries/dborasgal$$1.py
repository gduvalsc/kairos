class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGAL$$1",
            "collections": [
                "DBORASGA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, pool||' '||name as label, size as value from DBORASGA where pool = 'large') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)