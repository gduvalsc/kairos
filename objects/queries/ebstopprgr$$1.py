class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSTOPPRGR$$1",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, prg_name as label, executecount * 1.0 / ebscoeff() as value from EBS12CM where prg_name not like 'FNDRS%'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)