class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGA$$3",
            "collections": [
                "DBORAPGA"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Memory allocated' label, sum(value) value from (select timestamp, 'xxx' label, memalloc value from DBORAPGA) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)