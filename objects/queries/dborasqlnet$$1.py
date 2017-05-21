class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQLNET$$1",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [
                "match"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, value / 1024.0 value from DBORASTA where match(statistic, '(bytes)')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)