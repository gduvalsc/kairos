class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGONS$$2",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'logon rate' as label , sum(value) as value from (select timestamp, statistic as label, value as value from DBORASTA where statistic in ('logons cumulative')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)