class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATIMEMODEL",
            "collection": "DBORATMS",
            "filterable": True,
            "userfunctions": ['match'],
            "request": "select timestamp, statistic label, sum(time) value from DBORATMS where match(statistic, '^.*elapsed') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
