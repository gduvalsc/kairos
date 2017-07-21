class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUM1$$2",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, value / 100.0 value from DBORASTA where statistic='CPU used by this session') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)