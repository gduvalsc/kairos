class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERSQLWAIT$$1",
            "collections": [
                "SNAPPER"
            ],
            "userfunctions": [
                "snappercoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sql_id as label, pthread / 100 /snappercoeff() as value from SNAPPER where event != 'ON CPU' and sql_id != '') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)