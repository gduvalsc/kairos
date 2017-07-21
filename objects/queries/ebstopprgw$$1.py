class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSTOPPRGW$$1",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, prg_name label, waitcount * 1.0 / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)