class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGONS2",
            "collection": "DBORASTA",
            "request": "select timestamp, 'logon rate' label, sum(value) value from DBORASTA where statistic in ('logons cumulative') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
