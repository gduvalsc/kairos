class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGA$$2",
            "collections": [
                "DBORAPGA"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Memory other allocated'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, memalloc - memused as value from DBORAPGA) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)