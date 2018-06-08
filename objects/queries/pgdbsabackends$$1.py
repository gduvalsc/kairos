class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBSABACKENDS$$1",
            "collections": [
                "vkpg_stat_activity"
            ],
            "userfunctions": [
                "pgdbscoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, datname as label, 1.0 / pgdbscoeff(cast(snap_frequency as integer)) as value from vkpg_stat_activity where state = 'active') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)