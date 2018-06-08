class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISK$$3",
            "collections": [
                "NMONDISKBUSY"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, 'Busy rate'::text as label, value as value from NMONDISKBUSY where id = '%(NMONDISK)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)