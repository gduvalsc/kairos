class UserObject(dict):
    def __init__(s):
        if "DBORAHSQLTS" not in kairos: kairos['DBORAHSQLTS']=''
        object = {
            "type": "query",
            "id": "DBORAHSQLTSWC",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'Concurrency' label, sum(ccwait_delta / 1000000.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where sql_id = '" + kairos["DBORAHSQLTS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
