class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONPROCAIO$$2",
            "collections": [
                "NMONPROCAIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, id as label, value as value from NMONPROCAIO where id in ('aiocpu')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)