class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLVCPU$$3",
            "collections": [
                "NMONCPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Logical CPU (computation 1) %' label, avg(value) value from (select timestamp, 'xxx' label, user + sys value from NMONCPU where id = 'ALL') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)