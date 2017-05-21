class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLVCPU$$4",
            "collections": [
                "NMONCPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Logical CPU (computation 2) %' label, avg(value) value from (select timestamp, 'xxx' label, value value from (select timestamp, sum(user + sys) / count(cpus) value from NMONCPU where id != 'ALL' group by timestamp)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)