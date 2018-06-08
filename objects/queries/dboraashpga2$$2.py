class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHPGA2$$2",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'PGA allocated'::text as label, pga_allocated as value from ORAHAS) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)