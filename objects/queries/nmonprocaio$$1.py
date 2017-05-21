class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONPROCAIO$$1",
            "collections": [
                "NMONPROCAIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONPROCAIO where id in ('aioprocs','aiorunning')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)