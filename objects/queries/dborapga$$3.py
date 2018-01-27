class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGA$$3",
            "collections": [
                "DBORAPGA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Memory allocated'::text as label, memalloc as value from DBORAPGA) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)