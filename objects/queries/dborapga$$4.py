class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGA$$4",
            "collections": [
                "DBORAPGA"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'PGA aggregate target'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, aggrtarget as value from DBORAPGA) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)