class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXADSKOSIOFU$$1",
            "collections": [
                "EXATOPDSKOSIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, disk as label, putil as value from EXATOPDSKOSIO where type like 'F/%') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)