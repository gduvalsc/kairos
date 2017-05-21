class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONNETWA$$1",
            "collections": [
                "NMONNET"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value / 1024.0 value from NMONNET where id like '%write%') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)