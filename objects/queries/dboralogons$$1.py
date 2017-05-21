class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGONS$$1",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'user transactions' label, sum(value) value from (select timestamp, statistic label, value value from DBORASTA where statistic in ('user rollbacks', 'user commits')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)