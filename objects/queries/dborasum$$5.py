class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUM$$5",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, statistic as label, value as value from DBORASTA where statistic='physical reads') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)