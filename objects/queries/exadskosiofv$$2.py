class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXADSKOSIOFV$$2",
            "collections": [
                "EXATOPDSKOSIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, 'Flash device maximum capacity' label, 343.0 value from EXATOPDSKOSIO) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)