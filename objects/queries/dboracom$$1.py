class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACOM$$1",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, value value from DBORASTA where statistic in ('user commits', 'user rollbacks', 'transaction rollbacks')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)