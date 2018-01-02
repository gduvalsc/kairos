class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXACLLOSIODV$$2",
            "collections": [
                "EXATOPCLLOSIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , avg(value) as value from (select timestamp, 'Flash disk maximum capacity for cell'::text as label, 1332.0::real as value from EXATOPCLLOSIO) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)