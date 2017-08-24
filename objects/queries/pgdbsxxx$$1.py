class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBSXXX$$1",
            "collections": [
                "vkpg_stat_activity"
            ],
            "userfunctions": [
                "pgdbscoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, datname label, 1.0 / pgdbscoeff() value from vkpg_stat_activity) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)