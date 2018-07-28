class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERSCHWEV$$1",
            "collections": [
                "SNAPPER"
            ],
            "userfunctions": [
                "snappercoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, case when event is null then 'on cpu' when event is not null then event end as label, pthread / 100 /snappercoeff() as value from SNAPPER where username = '%(SNAPPERSCHWEV)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)