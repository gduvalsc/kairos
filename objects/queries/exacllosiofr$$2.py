class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXACLLOSIOFR$$2",
            "collections": [
                "EXATOPCLLOSIO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, 'Flash disk maximum capacity for cell' label, 35716.0 value from EXATOPCLLOSIO) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)