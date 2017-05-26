class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSPRGEXEW$$1",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, request_id||' (duration: '||cast(time * 60.0 as text)||')' label, waitcount * 1.0 / ebscoeff() value from EBS12CM where prg_name = '%(EBSPRGEXEW)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)