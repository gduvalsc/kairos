class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGA$$5",
            "collections": [
                "DBORAPGC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'One pass execs' label, sum(value) value from (select timestamp, 'xxx' label, value value from (select c.timestamp timestamp, execs1 * elapsed value from DBORAPGC c, DBORAMISC m where c.timestamp = m.timestamp)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)