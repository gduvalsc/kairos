class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGA$$1",
            "collections": [
                "DBORAPGA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Workarea (Manual + Auto) allocated'::text as label, memused as value from DBORAPGA) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)