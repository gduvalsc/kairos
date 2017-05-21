class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONIOADAPTWA$$2",
            "collections": [
                "NMONIOADAPT"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'All adapters (write)' label, sum(value) value from (select timestamp, 'xxx' label, value / 1024.0 value from NMONIOADAPT where id like '%write%') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)