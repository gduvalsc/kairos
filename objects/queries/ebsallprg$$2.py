class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSALLPRG$$2",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, 'Waiting programs'::text as label, sum(value) as value from (select timestamp, 'xxx'::text as label, waitcount * 1.0 / ebscoeff() as value from EBS12CM where prg_name not like 'FNDRS%'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)