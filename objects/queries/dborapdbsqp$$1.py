class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPDBSQP$$1",
            "collections": [
                "DBORASQP"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sqlid as label, parses as value from DBORASQP where pdb = '%(DBORAPDBSQP)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)