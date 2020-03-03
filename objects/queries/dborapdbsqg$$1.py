class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPDBSQG$$1",
            "collections": [
                "DBORASQG"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sqlid as label, gets as value from DBORASQG where pdb = '%(DBORAPDBSQG)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)