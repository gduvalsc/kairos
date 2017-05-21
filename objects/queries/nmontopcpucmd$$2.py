class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPCPUCMD$$2",
            "collections": [
                "NMONTOP"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'All captured commands' label, sum(value) value from (select timestamp, 'xxx' label, (value+0) / 100.0 value from NMONTOP where id = '%CPU') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)