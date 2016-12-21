class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPULV4",
            "collection": "NMONCPU",
            "request": "select timestamp, 'Logical CPU (computation 2) %' label, avg(value) value from (select timestamp, 'x' label, sum(user + sys) / count(cpus) value from NMONCPU where id != 'ALL' group by timestamp, label) group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
