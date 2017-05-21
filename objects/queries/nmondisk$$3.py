class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISK$$3",
            "collections": [
                "NMONDISKBUSY"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Busy rate' label, avg(value) value from (select timestamp, 'xxx' label, value value from NMONDISKBUSY where id = '%(NMONDISK)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)