class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARCPU$$1",
            "collections": [
                "SARU"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'sys' label, sys value from SARU where cpuid = 'all' union all select timestamp, 'usr' label, usr value from SARU where cpuid = 'all') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)