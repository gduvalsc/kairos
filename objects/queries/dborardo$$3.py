class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDO$$3",
            "collections": [
                "DBORAWEB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, event label, time value from DBORAWEB where event in ('log file parallel write', 'LGWR wait on LNS')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)