class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUME$$1",
            "collections": [
                "DBORATMS"
            ],
            "userfunctions": [
                "meet"
            ],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, statistic as label, time as value from DBORATMS where meet(statistic, '^.*elapsed')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)