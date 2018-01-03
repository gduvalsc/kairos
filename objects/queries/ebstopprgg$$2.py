class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSTOPPRGG$$2",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, 'All programs with status G'::text as label, sum(value) as value from (select timestamp, 'xxx'::text as label, executecount * 1.0 / ebscoeff() as value from EBS12CM where status_code = 'G'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)