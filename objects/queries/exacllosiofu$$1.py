class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXACLLOSIOFU$$1",
            "collections": [
                "EXATOPCLLOSIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, type || ' - ' || cell label, putil value from EXATOPCLLOSIO where type like 'F/%') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)