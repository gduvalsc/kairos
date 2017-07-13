class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBSCTRANSACTIONS$$2",
            "collections": [
                "vkpg_stat_activity"
            ],
            "userfunctions": [
                "pgdbscoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'All backends' label, 1.0 / pgdbscoeff(cast(snap_frequency as integer)) value from vkpg_stat_activity where datname = '%(PGDBSCTRANSACTIONS)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)