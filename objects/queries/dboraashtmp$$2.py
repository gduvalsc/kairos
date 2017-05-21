class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHTMP$$2",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, 'Temp space allocated' label, sum(value) value from (select timestamp, 'xxx' label, temp_space_allocated value from ORAHAS) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)