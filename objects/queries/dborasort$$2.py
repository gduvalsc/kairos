class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASORT$$2",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [
                "match"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, value value from DBORASTA where match(statistic, '(sort.*rows)')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)