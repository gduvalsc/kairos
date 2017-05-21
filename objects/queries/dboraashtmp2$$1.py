class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHTMP2$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sql_id label, temp_space_allocated value from ORAHAS where sql_id != '') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)