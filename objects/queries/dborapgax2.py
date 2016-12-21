class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGAX2",
            "collection": "DBORAPGC",
            "request": "select c.timestamp timestamp, 'Multi pass execs' label, sum(execs2 * elapsed) value from DBORAPGC c, DBORAMISC m where c.timestamp = m.timestamp group by c.timestamp, label order by c.timestamp"
        }
        super(UserObject, s).__init__(**object)
