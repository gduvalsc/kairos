class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBSCBACKENDS$$1",
            "collections": [
                "vkpg_stat_activity"
            ],
            "userfunctions": [
                "pgdbscoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'Active backends' label, 1.0 / pgdbscoeff(cast(snap_frequency as integer)) value from vkpg_stat_activity where datname = '%(PGDBSCBACKENDS)s' and state = 'active'  union all select timestamp, 'All backends' label, 1.0 / pgdbscoeff(cast(snap_frequency as integer)) value from vkpg_stat_activity where datname = '%(PGDBSCBACKENDS)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)