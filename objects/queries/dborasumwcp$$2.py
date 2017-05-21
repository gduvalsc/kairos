class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUMWCP$$2",
            "collections": [
                "DBORATMS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'DB CPU' label, sum(value) value from (select timestamp, statistic label, time value from DBORATMS where statistic='DB CPU') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)