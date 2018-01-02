class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHTMP2$$2",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, 'Temp space allocated'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, temp_space_allocated as value from ORAHAS) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)