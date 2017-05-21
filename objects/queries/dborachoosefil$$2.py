class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEFIL$$2",
            "collections": [
                "DBORAFIL"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'number of reads per sec' label, sum(value) value from (select timestamp, 'xxx' label, reads value from DBORAFIL where file='%(DBORAFIL)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)