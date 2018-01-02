class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONPAGE$$1",
            "collections": [
                "NMONPAGE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, id as label, value as value from NMONPAGE where id in ('pgin', 'pgout', 'pgsin', 'pgsout')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)