class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXADSKOSIODW$$1",
            "collections": [
                "EXATOPDSKOSIOL"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, disk label, wtime value from EXATOPDSKOSIOL where type like 'H/%') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)