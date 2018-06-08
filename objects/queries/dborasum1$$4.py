class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUM1$$4",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, statistic as label, value as value from DBORASTA where statistic='session logical reads') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)